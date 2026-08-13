# The pilot AI workstation: proving the product on the desktop

> **NOTE** Draft status: rough draft, written 2026-08-13 on the laptop,
> before any software has been installed on the target machine. Every
> stack fact below is verified against vendor documentation and says so,
> with the date it was read. Nothing has yet been verified against the
> machine itself: steps are marked **planned** until they have been run
> on the desktop, and only then promoted to instruction, per the
> project's verify-before-teaching rule. Final prose is the creator's.

## What this pilot is for

The project now has a working product hypothesis, recorded in
`project_log.md` Entry 080: an AI workstation installed on a small
organisation's own premises, running models locally or in a
local-plus-API hybrid, carrying workflows built for that organisation's
actual work, with enough onboard guidance to teach its own proper use.

Before that idea is put in front of anyone, it has to run. The
project's existing desktop PC is the testbed, and the pilot answers
three questions in order:

1. Does hardware the project already owns serve a useful model at a
   usable speed? (Phase 1)

2. Does the deployment shape work: the same thing, but as Linux
   containers that could be stood up on a customer's machine rather
   than hand-installed apps? (Phase 2)

3. Is the capability *adequate* for the work a small organisation would
   actually give it? (Phase 3 — the question
   `drafts/budget_vram_for_local_ai.md` ends on, and the one that
   decides whether the product is honest to sell.)

What this pilot deliberately does not answer: **the Intel question.**
The desktop carries an AMD card, so everything here exercises the AMD
half of the open stack (ROCm and Vulkan). The Arc Pro line's own
software story — SYCL, the archived IPEX-LLM, LLM Scaler — can only be
tested on an Arc card, and that purchase is now made
(`project_log.md` Entry 081). See "Where the Arc question fits" at
the end.

## The machine

| Part | Spec | What it means for the pilot |
|---|---|---|
| CPU | Ryzen 7 7800X3D (8 cores) | More than enough to feed one GPU. |
| RAM | 32 GB | Fine for running models. Not enough for converting them: one logged quantisation conversion consumed ~54 GiB of system RAM (`[BENTECH-ARC26]`, via the VRAM document). Download pre-quantised files instead of converting locally. |
| GPU | Radeon RX 7900 XT, 20 GB VRAM | The number that decides everything else. See below. |
| Cooling | High-quality air/liquid, well ventilated | Generation is a sustained load, not a burst; thermals get noted during measurement, not assumed. |

20 GB sits between the two tiers the VRAM document prices. Against its
capacity table: the 16 GB class (12–14B dense models, 20B-class
mixture-of-experts) fits with room to spare; the 24 GB class (27–32B
dense at 4-bit) is the stretch, and the largest of those will not leave
enough free VRAM for a long context. The comfortable target class for
this card is roughly 20–30B mixture-of-experts and up to ~24B dense at
4-bit, keeping 2–3 GB free for context.

> **TIP** Model names move fast, so this unit names classes and lets
> the operator pick current releases at install time. The models the
> project has already benchmarked from published sources — Mistral
> Small 24B, the 30–35B-A3B mixture-of-experts family — mark the
> classes worth starting with. A 24B dense pick has a bonus: it is the
> model the `[SR-B70-26]` review measured on Arc hardware, which keeps
> a like-for-like thread open if an Arc card arrives later.

## Phase 1 — first tokens, native Windows

**Goal:** the GPU serving a current ~20–30B-class model on Windows,
confirmed to be running on the GPU and not silently on the CPU, with
first measurements recorded.

**Verified against documentation (2026-08-13):**

- Ollama's GPU documentation lists the Radeon RX 7900 XT as supported
  on Windows, and states the requirement as an AMD ROCm v7 /
  HIP7-capable **driver** stack — the ordinary current Adrenalin
  driver, not a separate ROCm SDK install.

- Ollama also carries a Vulkan backend with its own controls
  (`OLLAMA_VULKAN=0` disables it; `GGML_VK_VISIBLE_DEVICES` selects
  devices). Two backends on one card is the same shape as the Arc
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
   account, no telemetry decisions beyond the installer's own prompts —
   read them rather than clicking through.

4. **Pull one model sized to the card.** Check the file size on the
   model page before pulling: it should sit well under 20 GB. One
   ~24B dense at 4-bit, one ~30B-A3B mixture-of-experts; nothing else
   until both are measured.

5. **First run with statistics on:** `ollama run <model> --verbose`.
   The stats block after each reply is the phase's whole point — read
   it, don't skim it:

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

> **TIP** LM Studio is the no-terminal route to the same card, with
> ROCm and Vulkan runtimes on Windows, and it matters to this project
> for exactly that reason: it is the shape of tool a learner without a
> terminal habit would actually use, which is the audience the product
> serves. Its current 7900-series support is **not yet verified** by
> this unit — check its documentation at install time if this route is
> taken. Phase 1 measurements use Ollama either way, for comparability.

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
| Prompt eval rate / eval rate | The two speeds, kept separate. |
| VRAM used (Task Manager) | Confirms placement and shows context headroom. |
| Notes | Thermals, noise, anything odd. By ear is fine at this stage. |

Three runs per prompt; report the middle eval rate, which resists the
odd stall better than an average.

> **WARNING** Published serving benchmarks are a different measurement.
> The `[SR-B70-26]` figures the VRAM document quotes are batch-32
> serving throughput — many simultaneous requests. Single-stream
> numbers from this protocol will be far lower and are not comparable.
> Comparing across that line is the same three-tier confusion the
> project flagged as a teaching case in `project_log.md` Entry 078.

## Phase 2 — the deployment shape (WSL2, Docker, vLLM)

**Goal:** the same card serving an OpenAI-compatible endpoint from a
Linux container, with a web front-end in a second container — the form
a deployed workstation would actually take, administered without
touching the model runtime.

**Verified against documentation (2026-08-13):**

- AMD's WSL compatibility matrix (ROCm 7.2.1) lists the Radeon RX
  7900 XT as supported under WSL2, on Ubuntu 24.04 or 22.04, with
  PyTorch, ONNX and TensorFlow at official production support.

- vLLM supports the 7900 series' architecture (gfx1100) upstream,
  added without flash-attention — so some engine features are gated on
  this card class, and that is expected rather than a fault.

- **Not yet verified:** which current vLLM release/container actually
  serves gfx1100 out of the box, and whether the ROCm-under-WSL2 path
  runs vLLM specifically — AMD's matrix names the three frameworks
  above and stops. These two facts get settled against vLLM's own AMD
  installation documentation, on the machine, before this phase's
  steps are written up as instruction.

**Planned steps** (outline only, for the reason above):

1. `wsl --install` — installs WSL2 and a default Ubuntu, needs
   virtualisation enabled in BIOS and one reboot.

2. Cap WSL2's memory in `.wslconfig` (around 16 GB of the 32): WSL2
   grows to take most of the host's RAM otherwise, and the host still
   needs to function.

3. GPU access per AMD's WSL page: the *Windows* driver carries the
   GPU path into WSL; inside the distribution only user-space ROCm is
   added. No kernel driver gets installed in Linux, which surprises
   people who have done this on bare metal.

4. Docker Engine inside the distribution, not Docker Desktop — closer
   to the deployment shape, and Docker Desktop carries per-seat
   licensing above a size threshold that a customer organisation would
   have to check; Engine does not.

5. vLLM's ROCm route per its own docs; smoke-test the endpoint with a
   one-line request before any front-end; then a web UI container
   (Open WebUI class) pointed at the endpoint.

## Phase 3 — the task set and the tutor layer (design only)

Not specified until phases 1–2 produce numbers. The shape, from the
VRAM document's closing sketch and the product hypothesis:

- A fixed task set shaped like SME work — batch classification,
  extraction, drafting against a house style — run entirely locally,
  scored for *adequacy* against the late-2024-class capability ceiling
  the project logged for single-card models (`research_log.md`
  Entry 079).

- The tutor layer: the machine's own front-end carrying guidance on
  proper use — the project's teaching material where it is needed, at
  the moment of use. This is the part of the hypothesis nothing else
  in the market bundles, and it stays a sketch until the serving layer
  under it exists.

## Where the Arc question fits

This pilot proves the product shape on hardware the project already
owns, for nothing. It does not touch the Intel stack, which is the
VRAM document's central open question.

That card is now decided: the **Arc Pro B70**, 32 GB, ~£1,290 at the
2026-08-11 price snapshot — chosen over the cheaper B580 and B60
because 32 GB is the tier the project's own findings converge on
(`project_log.md` Entry 081). The measurement protocol above runs on
it unchanged, which is what it was built for, and the comparison the
project has so far only read about becomes one it has measured.
Buying the card settles nothing on its own; the numbers still have to
be produced.

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

Findings from running this unit land in `research_log.md` as normal
dated entries; this file is procedure, not findings.
