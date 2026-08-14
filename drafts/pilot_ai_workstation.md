# The pilot AI workstation

*Proving the product on the desktop*

> **NOTE** Draft status: rough draft, written 2026-08-13 on the laptop,
> before any software has been installed on the target machine. Every
> stack fact below is verified against vendor documentation and says so,
> with the date it was read. Steps are marked **planned** until they
> have been run on the desktop, and only then promoted to instruction,
> per the project's verify-before-teaching rule. Final wording is the
> creator's.
>
> Revised 2026-08-14 on the desktop itself: the hardware table now
> carries what the machine reports rather than what was remembered, and
> the Arc card's host is decided (`project_log.md` Entry 083). The
> software steps remain unrun.

## What this pilot is for

The project now has a working product hypothesis, recorded in
`project_log.md` Entry 080: an AI workstation installed on a small
organisation's own premises, running models locally or in a
local-plus-API hybrid, carrying workflows built for that organisation's
actual work, with enough onboard guidance to teach its own proper use.

The last clause is the point of the whole thing. The machine carries a
tutor layer: its own front-end, holding guidance on proper use, built
eventually on self-populated user profiles. This is where real
practical AI skills can be developed: the user learns by logging onto
the workstation and asking questions. It makes people self-sufficient,
able to improve and refine their own understanding and workflows
independently, and nothing else found so far bundles it with the
hardware. One small, custom deployed AI workstation could act as a
realistic, grass-roots alternative to training that is currently
centred around medium/large organisations and cloud computing.

Before that idea is put in front of anyone, it has to run. The
project's existing desktop PC is the testbed, and the pilot answers
three questions in order:

1. Does hardware the project already owns serve a useful model at a
   usable speed? (Phase 1)

2. Does the deployment shape work: the same thing, but as Linux
   containers that could be stood up on a customer's machine rather
   than hand-installed apps? (Phase 2)

3. Is the capability *adequate* for the work a small organisation would
   actually give it? (Phase 3)

What phases 1–3 deliberately do not answer: **the Intel question.**
The desktop currently carries an AMD card, so those phases exercise
the AMD half of the open stack (ROCm and Vulkan). The Arc Pro line's
own software story — SYCL, OMIX, the archived IPEX-LLM, LLM Scaler —
can only be tested on an Arc card. That purchase is now made
(`project_log.md` Entry 081) and the card goes in this same machine
(Entry 083), which is why the AMD phases are sequenced first: the two
cards share one usable slot. See "Where the Arc card goes" at the
end.

![One machine, two card eras: the AMD phases run on Windows and WSL2, the Arc phase on native Linux, and the two cards share one PCIe 4.0 x16 slot — swap, not stack.](../assets/figures/fig_pilot_stacks.png)

## The machine

| Part | Spec | What it means for the pilot |
|---|---|---|
| CPU | Ryzen 7 7800X3D (8 cores) | More than enough to feed one GPU. AM5, so Resizable BAR is available — which is the Arc cards' actual platform requirement. |
| RAM | 32 GB | Fine for running models. Not enough for converting them: one logged quantisation conversion consumed ~54 GiB of system RAM (`[BENTECH-ARC26]`, via the VRAM document). Download pre-quantised files instead of converting locally. |
| Motherboard | MSI B650 GAMING PLUS WIFI (MS-7E26) | **One graphics-usable slot.** PCI_E1 runs PCIe 4.0 x16 from the CPU; PCI_E2 is Gen3 x1 from the chipset, which is not a graphics slot in any useful sense. Two GPUs therefore take turns rather than coexisting. Slot layout is from published specification, not yet confirmed by hand — MSI's site blocks automated reading. |
| GPU | Radeon RX 7900 XT, 20 GB VRAM | The number that decides everything else. See below. Confirmed negotiating Gen4 x16, which is this card's own ceiling. |
| PSU | Corsair RM1000x (2021), 1000 W, 80+ Gold, fully modular | Recorded 2026-08-14 from the unit. Ample headroom for either card — and the one-slot board means the ~315 W Radeon and the 230 W-TBP B70 never draw together. The swap-risk check from the first draft is closed. |
| Cooling | High efficiency air-cooled | Generation is a sustained load, not a burst; thermals get noted during measurement, not assumed. |

20 GB sits between the two tiers the VRAM document prices and
compares. Against its capacity table: the 16 GB class (12–14B dense
models, 20B-class mixture-of-experts) fits with room to spare. The
24 GB class (27–32B dense at 4-bit) is potentially less viable; the
largest of those will not leave enough free VRAM for a long context.
The comfortable target class for this card is roughly 20–30B
mixture-of-experts and up to ~24B dense at 4-bit, keeping 2–3 GB free
for context.

> **TIP** Model names move fast, so this unit names classes of models
> and lets the operator pick current releases at install time. The
> models the project has already benchmarked from published sources:
> Mistral Small 24B, the 30–35B-A3B mixture-of-experts family. A 24B
> dense pick has a bonus: it is the model the `[SR-B70-26]` review
> measured on Arc hardware, which keeps a like-for-like thread open if
> an Arc card arrives later.

## Phase 1 — first tokens, native Windows

**Goal:** the GPU serving a current ~20–30B-class model on Windows,
confirmed to be running on the GPU and not silently on the CPU, with
first measurements recorded.

**Verified against documentation (2026-08-13):**

- Ollama's GPU documentation lists the Radeon RX 7900 XT as supported
  on Windows. They state the requirement as an AMD ROCm v7 /
  HIP7-capable **driver** stack. This just means the current Adrenalin
  driver, not a separate ROCm SDK install.

- Ollama also carries a Vulkan backend with its own controls.
  `OLLAMA_VULKAN=0` disables it and `GGML_VK_VISIBLE_DEVICES` selects
  devices. Two backends on one card is the same shape as the Arc
  document's Vulkan/SYCL split, and worth remembering when a result
  looks odd: which backend served it is part of the result.

- AMD's own Windows compatibility matrix (ROCm 6.4.4 page) lists the
  7900 series on Windows 11 and adds the honest caveat that the entire
  ROCm stack is not yet supported on Windows. That caveat is about the
  full SDK; it does not block Ollama's driver-level route.

**Planned steps** (run on the desktop; each one says what it does):

1. **Update the GPU driver first.** AMD Adrenalin, current WHQL
   release. This is Ollama's stated dependency for AMD on Windows, and
   driver age is the first suspect in any backend failure.

2. **Check disk space before pulling models.** Quantised files in the
   target class run 12–20 GB each, and a testing session accumulates
   several.

3. **Install Ollama for Windows** from ollama.com. The installer adds
   a background service, the `ollama` command, and a tray app. No
   account, no telemetry decisions beyond the installer's own prompts,
   so read them rather than clicking through.

4. **Pull one model sized to the card.** Check the file size on the
   model page before downloading; it should sit well under 20 GB. Pull
   one ~24B dense model at 4-bit and one ~30B-A3B mixture-of-experts
   model. Pull nothing else until both are measured.

5. **First run with statistics on:** `ollama run <model> --verbose`.
   The stats block after each reply is the whole point of this phase,
   so read it, don't skim it.

   - *prompt eval rate* is how fast the model reads the input
     (tokens/second on the prompt);

   - *eval rate* is how fast it writes — the number that decides
     whether it feels usable. Calibration from the VRAM document:
     people read at roughly 5 tokens/second, so above ~10 the machine
     is comfortably ahead of the reader.

6. **Confirm the GPU is doing the work.** `ollama ps` shows how much
   of the loaded model sits on GPU versus CPU — the pass mark is
   100% GPU. Cross-check in Task Manager → Performance → GPU:
   dedicated memory should jump by roughly the model file's size when
   it loads.

7. **Know what failure looks like before it happens.** Single-digit
   eval rate, busy CPU, flat VRAM: that is CPU fallback, not a slow
   GPU. Check, in order: driver version against Ollama's requirement;
   whether the model file exceeded free VRAM (spill); the server log,
   which names the backend it loaded and the devices it found.

> **TIP** LM Studio is the GUI route to the same card, with ROCm and
> Vulkan runtimes on Windows, and it matters to this project for
> exactly that reason: it is the type of tool a learner without prior
> CLI experience would be comfortable using. This demographic (workers
> with relatively low technical knowledge) is the exact audience the
> product serves. LM Studio RX 7900 series support is **not yet
> verified** by this unit. Check the documentation at install time if
> this route is taken. Phase 1 measurements use Ollama either way, for
> comparability.

## The measurement protocol

Every published number the VRAM document rests on was measured on
someone else's rig — three of its five benchmark sources ran on
vendor-supplied hardware. These are the project's first own-hardware
measurements, so they are worth doing in a form that can be logged and
repeated.

**The fixed prompt set.** Three prompts, shaped like the work the
product claims, identical on every run and on every future card:

1. **Drafting:** *"Write a 150-word notice to customers announcing a
   two-day delay to all orders placed last week. Plain English,
   apologetic once, no excuses, no exclamation marks."*

2. **Summarisation:** *"Summarise the following document in five bullet
   points for a manager who has not read it."* — followed by a fixed
   test document chosen once and kept with the results (a public,
   ~2,000-word text; record its word count). The same document every
   run, or the numbers stop being comparable.

3. **Extraction:** *"Turn the following into a table with columns
   Name, Item, Quantity, Date."* — followed by this fixed block:

   ```text
   jones - 3 boxes A4 paper, weds
   Mrs Patel ordered two toner carts 14/8
   K. O'Neill: 1x desk lamp + 2 x HDMI cable, monday
   accounts (S Hughes) want 5 notepads and a stapler 15 aug
   D Kowalski — six AA batteries, no date given
   ```

**What to record per run**, one row per run in a results table kept
beside this file once measurement starts:

| Field | Why |
|---|---|
| Date, driver version, Ollama version | Results move with software; undated numbers are the trap the VRAM document warns about. |
| Model, quantisation tag, context length | The three settings that change the result most. |
| Prompt eval rate / eval rate | The two speeds, kept separate to avoid conflation. |
| VRAM used (Task Manager) | Confirms placement and shows context headroom. |
| Notes | Thermals, noise, anything odd. By ear is fine at this stage. |

Three runs per prompt; report the median eval rate. This resists the
odd stall better than a mean average.

> **WARNING** Published serving benchmarks are a different measurement.
> The `[SR-B70-26]` figures the VRAM document quotes are batch-32
> serving throughput — many simultaneous requests. Single-stream
> numbers from this protocol will be far lower and are not comparable.
> Comparing across that line is the same three-tier confusion the
> project flagged as a teaching case in `project_log.md` Entry 078.

## Phase 2 — the deployment shape (WSL2, Docker, vLLM)

**Goal:** the same card serving an OpenAI-compatible endpoint from a
Linux container, with a web front-end in a second container. This is
the form a deployed workstation would actually take, administered
without touching the model runtime.

> **WARNING** This phase is **the AMD card's route only.** WSL2 works
> here because AMD's compatibility matrix supports the 7900 XT under
> it. No vendor documentation places a B-series Arc card under WSL2;
> PyTorch's validated client-GPU list names Windows 11 and Ubuntu, and
> Intel's IPEX documentation explicitly excludes B-series from WSL2
> (`research_log.md` Entry 087). The Arc half of this phase runs on
> native Linux instead; see the closing section.

**Verified against documentation (2026-08-13):**

- AMD's WSL compatibility matrix (ROCm 7.2.1) lists the Radeon RX
  7900 XT as supported under WSL2, on Ubuntu 24.04 or 22.04, with
  PyTorch, ONNX and TensorFlow at official production support.

- vLLM supports the 7900 series' architecture (gfx1100) upstream,
  added without flash-attention, so some engine features are gated on
  this card class. That is expected rather than a fault.

- **Not yet verified:** which current vLLM release/container actually
  serves gfx1100 out of the box, and whether the ROCm-under-WSL2 path
  runs vLLM specifically - AMD's matrix names the three frameworks
  above and stops. These two facts get settled against vLLM's own AMD
  installation documentation before this phase's steps are written up
  as instruction.

**Planned steps** (outline only, for the reason above):

1. `wsl --install` installs WSL2 and a default Ubuntu, needs
   virtualisation enabled in BIOS and one reboot.

2. Cap WSL2's memory in `.wslconfig` (around 16 GB of the 32): WSL2
   grows to take most of the host's RAM otherwise, and the host still
   needs to function.

3. GPU access per AMD's WSL page: the *Windows* driver carries the
   GPU path into WSL; inside the distribution only user-space ROCm is
   added. No kernel driver gets installed in Linux, which surprises
   people who have done this on bare metal.

4. Docker Engine inside the distribution, not Docker Desktop. This is
   closer to the deployment shape, and Docker Desktop carries per-seat
   licensing above a size threshold that a customer organisation would
   have to check; Engine does not.

5. vLLM's ROCm route per its own docs; smoke-test the endpoint with a
   one-line request before any front-end; then a web UI container
   (Open WebUI class) pointed at the endpoint.

## Phase 3 — the task set and the tutor layer (design only)

Not specified until phases 1–2 produce numbers. The shape, from the
VRAM document's closing sketch and the product hypothesis:

- **A fixed task set**, run entirely locally and scored for *adequacy*
  against the late-2024-class capability ceiling the project logged
  for single-card models (`research_log.md` Entry 079). Two
  candidates, at different stages of maturity:

  - *Candidate one, ordinary SME work:* batch classification,
    extraction, drafting against a house style. This is the one the
    measurement protocol above already fits.

  - *Candidate two, medical RAG workflows:* what this means in
    practice is currently undecided.

- **The tutor layer**, whose purpose is stated in "What this pilot is
  for" above. What Phase 3 must decide is narrower than the wider
  project vision: does guidance delivered at the moment of use, on a
  machine of this class actually teach anyone anything? It stays a
  sketch until the serving layer under it exists.

## Where the Arc card goes

Phases 1–3 prove the product shape on hardware the project already
owns, for nothing, and they exercise the AMD half of the open stack.
The Intel stack (the VRAM document's central open question) needs
Intel hardware, and that card is now decided: the **Arc Pro B70**,
32 GB, ~£1,290 at the 2026-08-11 price snapshot. This was chosen over
the cheaper B580 and B60 cards because 32 GB VRAM is the tier the
project's findings converge on (`project_log.md` Entry 081).

**It goes in this same desktop** (`project_log.md` Entry 083), reusing
the build above rather than the existing, always-on AM4 Ubuntu
server. The measurement
protocol runs on it unchanged, which is what the protocol was built
for, and the comparison the project has so far only read about becomes
one it has measured. Buying the card settles nothing on its own; the
numbers still have to be produced.

### What the host decides, and what it does not

Three things were checked before this was written, because each was a
plausible reason to spend money or change plan
(`research_log.md` Entry 087):

- **An Intel motherboard and CPU are not required.** Resizable BAR is
  the cards' actual platform requirement, an AM5 Ryzen 7000 system
  provides it, and Intel's own documentation allows for non-Intel
  platforms with ReBAR or Smart Access Memory enabled. What a board
  change would buy is slot topology, not compatibility.

- **The two cards take turns.** One graphics-usable slot means the
  7900 XT comes out when the B70 goes in. This sequences the work
  rather than changing it: finish phases 1–2 on the Radeon, then swap.
  It also rules out the two-card configurations discussed elsewhere —
  a board limit, not a vendor one.

- **WSL2 is not a documented path for this card.** Which makes the
  operating system, rather than the machine, the remaining open
  question.

### The three OS routes

Two requirements converge here. Phase 2 needs native Linux for the Arc
card, on the evidence above; the shared environment agreed with the
external correspondent independently assumes Ubuntu 26.04. The route
that satisfies the project's own next step is the one that keeps the
two environments comparable. The three options, against that:

| Route | What it gets | What it costs |
|---|---|---|
| Native Windows 11 | Validated PyTorch XPU; Ollama's Vulkan backend. Enough for Phase 1 numbers. | No OMIX, no Intel-validated containers, no Phase 2 deployment shape. Diverges from the shared environment agreed with the external correspondent, so results stop being comparable. |
| Dual-boot Ubuntu 26.04 | Everything: OMIX, the B70-validated containers, the full verification path, and an environment matching the collaboration. | A reboot between the AMD and Intel halves of the pilot. |
| Ubuntu outright | The same, without the reboot. | The desktop stops being a Windows desktop. |

![Where each card's stack is documented, per the vendors' own pages: every Intel-validated route to the B70 runs on native Linux — the OS the shared environment agreement already assumes.](../assets/figures/fig_pilot_os_matrix.png)

### Before the card arrives

Two checks remain, neither needing the card in hand:

1. **MSI's slot specification, read by hand.** Their site blocks
   automated reading, so PCI_E2 and PCI_E3 are published-spec only.

2. **ReBAR and Above 4G Decoding confirmed in BIOS** – confirmed
   enabled, not assumed.

The third from the first draft is closed: the PSU is a Corsair
RM1000x (2021), 1000 W, 80+ Gold — read off the unit 2026-08-14, and
not a constraint on any configuration this board allows.

Then the bring-up order, which the Intel documentation and the
correspondent's checkpoint document agree on: confirm the board and
its power requirement, confirm OS and a kernel 6.17-class Xe driver,
verify the card enumerates (device E223) and binds, verify it through
Level Zero and OpenCL, then prove real tensor work under
`torch.xpu` — before any model is loaded and any number is believed.

## Sources

Read directly 2026-08-13, official documentation only; the SEO-blog
guides that surface on these search terms were used as leads and carry
no claim in this unit:

- Ollama GPU documentation (docs.ollama.com/gpu) — RX 7900 XT on
  Windows; ROCm v7/HIP7 driver requirement; Vulkan controls.

- AMD ROCm compatibility matrix, Windows, ROCm 6.4.4
  (rocm.docs.amd.com) — 7900 series on Windows 11; full-stack caveat.

- AMD ROCm compatibility matrix, WSL, ROCm 7.2.1
  (rocm.docs.amd.com) — RX 7900 XT under WSL2; Ubuntu 24.04/22.04;
  framework support.

- vLLM upstream gfx1100 support (vllm-project PR #2768) — read at
  search level; confirm against current vLLM AMD docs at phase 2.

Read directly 2026-08-14, for the Arc host section
(`research_log.md` Entries 086–087): PyTorch's Intel-GPU
getting-started page (validated client OS list); Intel's dgpu-docs
(OMIX install guide and support matrix, Xe driver table) and IPEX
end-of-life page; Ollama's GPU and Docker pages; and the machine
itself, read via CIM and PnP device properties. The figures carry
these facts; their brand marks are identification, not endorsement.

Findings from running this unit land in `research_log.md` as normal
dated entries; this file is procedure, not findings.
