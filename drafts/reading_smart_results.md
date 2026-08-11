# Reading a drive's SMART results

A drive keeps its own health records. SMART — Self-Monitoring, Analysis
and Reporting Technology — is the part of a drive's firmware that counts
its errors, tracks its age and temperature, and runs self-tests on
request. The operating system does not grade the drive; the drive grades
itself, and `smartctl` is how you ask to see the marking.

This unit covers reading those records: the one command that shows
everything, the five numbers that decide whether a drive can be trusted,
and the two traps that make healthy drives look dying and dying drives
look healthy.

> **NOTE** — A self-test runs inside the drive, not on the computer. The terminal that started it will never print a result, and closing that terminal changes nothing. The result waits in the drive's own log until something asks for it.

## The command

```bash
sudo smartctl -H -A -l selftest /dev/sda
```

| Part | What it does |
|---|---|
| `sudo` | Drive-level queries need administrator rights. |
| `smartctl` | The control tool from the `smartmontools` package. |
| `-H` | The drive's overall verdict on itself — one line, `PASSED` or `FAILED`. |
| `-A` | The attribute table: the drive's running counters. |
| `-l selftest` | The self-test log, including the test you started. |
| `/dev/sda` | Which drive to ask. |

> **TIP** — Device names are handed out at boot and can swap between boots: the drive called `sda` today can be `sdb` tomorrow. Before acting on any result, confirm you are reading the drive you think you are: `sudo smartctl -i /dev/sda` prints the model and serial number, which match the label on the physical drive.

Prefer a window? Ubuntu ships **Disks** (search the applications grid
for "Disks"). Select the drive, open the menu in the title bar, and
choose **SMART Data & Self-Tests**. Same numbers, same log, and it can
start and stop tests too.

## Three layers, three different weights

`smartctl` answers at three levels, and they are not equally
trustworthy.

1. **The overall verdict (`-H`)** is the weakest. `PASSED` means only
   that no counter has yet crossed its failure threshold — drives
   routinely report `PASSED` while visibly deteriorating. Treat it as
   "not already condemned", never as "healthy".

2. **The self-test log (`-l selftest`)** is the exam result. A long
   test reads every sector on the platter, so "completed without error"
   means the whole surface has actually been read, recently.

3. **The attribute table (`-A`)** is the continuous record. It is where
   deterioration shows first, and the *trend* across weeks matters more
   than any single reading.

## Reading the self-test log

The log lists recent tests, newest first:

```
Num  Test        Status                    Remaining  LifeTime(hours)
# 1  Extended    Completed without error       00%        10831
# 2  Short       Completed without error       00%         9905
```

| Status | Meaning | What to do |
|---|---|---|
| `Completed without error` | Every sector read cleanly. | The pass you wanted. |
| `Completed: read failure` | Bad media found; the log records where. | Treat the drive as failing — see the verdicts below. |
| `Self-test routine in progress` | Still running; the percentage counts *down* to 00%. | Wait. Nothing else. |
| `Interrupted (host reset)` | A reboot or suspend cut it short. | No verdict either way. Run it again. |
| `Aborted by host` | Something cancelled it. | Run it again. |

> **CHECK** — `LifeTime(hours)` is the drive's power-on-hours count at the moment that test ran. Compare it against `Power_On_Hours` in the attribute table: if the two match to within a few hours, the top entry is the test you just ran, not a relic from years ago.

## The five numbers that decide

Backblaze, which operates hundreds of thousands of drives and publishes
its failure statistics, tracks five SMART attributes as failure
predictors: in its data, **76.7% of failed drives showed a non-zero
value in at least one of these five** before failing. Read the
**RAW_VALUE** column for all of them.

| ID | Attribute | What it counts |
|---|---|---|
| 5 | `Reallocated_Sector_Ct` | Sectors that failed and were quietly replaced from the drive's spare pool. |
| 187 | `Reported_Uncorrect` | Errors the drive had to report back to the computer as uncorrectable. |
| 188 | `Command_Timeout` | Operations that took so long the drive gave up on them. **On Seagate drives this one is packed — see below.** |
| 197 | `Current_Pending_Sector` | Sectors failing to read *right now*, awaiting a verdict. |
| 198 | `Offline_Uncorrectable` | Sectors that could not be read even during the drive's own scans. |

A healthy drive shows **zero** for all five. The lifecycle behind the
two sector counts: a sector that fails a read goes *pending* (197). If
a later read succeeds, it leaves the list; if the spot is confirmed
bad, the drive swaps in a spare and the count moves to *reallocated*
(5). Reallocation is the drive consuming its finite stock of spares —
the mechanism working as designed, but the need for it is the warning.

> **WARNING** — The Seagate panic trap. On Seagate drives, `Raw_Read_Error_Rate` (1), `Seek_Error_Rate` (7) and `Hardware_ECC_Recovered` (195) show raw values in the millions or billions. These are not errors: Seagate packs the total count of operations into the same raw number alongside the error count, so it grows enormous on a perfectly healthy drive. Judge those three by their normalised `VALUE` holding steady against `THRESH`, or ignore them.

### `Command_Timeout` (188) is packed too

This is the exception to "read the five raw", and it catches people who
have already learned the rule above.

On Seagate drives, 188's raw value is **three 16-bit counters in one
number**, read from the low end:

| Bits | Counter |
|---|---|
| Lowest 16 | Total command timeouts |
| Middle 16 | Commands that took over 5 seconds |
| Highest 16 | Commands that took over 7.5 seconds |

Worked example. A raw value of **196611** looks catastrophic and is not.
Convert to hexadecimal — `196611 = 0x00030003` — then split into 16-bit
groups from the right:

```
0x0000    0x0003    0x0003
  |         |         |
  |         |         +--  3 command timeouts
  |         +------------  3 commands over 5 seconds
  +----------------------  0 commands over 7.5 seconds
```

Three timeouts, not 196,611. The arithmetic without hex, if you prefer:
divide by 65,536 for the middle field and take the remainder for the
lowest. `196611 ÷ 65536 = 3 remainder 3`.

> **CHECK** — Before treating any 188 value as alarming, decode it. A handful of timeouts over a drive's lifetime is unremarkable and often points at a cable or a power supply rather than the drive. What matters is the same as everywhere else here: whether it grows.

> **TIP** — `UDMA_CRC_Error_Count` (199) counts data corrupted on the way between the drive and the motherboard. A rising 199 with the five above at zero is a **cable** fault, not a drive fault: reseat or replace the SATA data cable. The count never resets, so what matters is whether it stops rising.

## The other columns, briefly

Each attribute row also carries `VALUE`, `WORST` and `THRESH` — a
normalised score that starts high (typically 100 or 200), falls as the
drive degrades, and fails when it meets `THRESH`; `WHEN_FAILED` says
whether that has ever happened. These columns are what the `-H` verdict
is built from, which is exactly why `-H` is slow to alarm: for the five
counters above, the raw value moves long before the normalised score
follows.

Two attributes are context rather than verdicts. `Power_On_Hours` (9)
is the drive's total working life, useful for judging how much a clean
record actually covers — a drive that has spent most of its years
switched off has had few chances to discover its own bad sectors, which
is precisely what a long test corrects. `Temperature_Celsius` (194)
should sit comfortably below about 40 °C in steady use.

## What the results decide

| Result | Verdict |
|---|---|
| Long test completed without error, all five counters at zero | Fit for its role. The surface has actually been read, end to end, recently. |
| Test passes, but a counter is small and non-zero | Usable, not trustworthy: nothing irreplaceable lives on it. Re-test in a few weeks — **growth is the signal, not the absolute number.** |
| Read failure, or counters climbing between checks | Plan its retirement. Copy anything wanted off it now, while it still reads, starting with what matters most. |

Attribute **187** deserves singling out. Backblaze's position on it is
unusually firm: drives with zero uncorrectable errors hardly ever fail,
and once 187 goes above zero they schedule the drive for replacement.
Their own qualifier matters as much as the rule, though — a drive going
from zero to twenty in a day is in a different situation from one
reporting a single error every few months for years. **A non-zero 187
means start watching properly, not panic**, and it means the drive
should not be the only copy of anything.

Note also whose rule it is. Backblaze replaces at the first sign because
a spare drive costs them less than an engineer visit; a household
weighing a working drive against buying a new one is doing different
arithmetic. Take the signal, judge the response yourself.

> **NOTE** — One clean pass is evidence, not immunity. Backblaze's same figure read the other way: roughly a quarter of its failed drives showed no warning in any of the five attributes. A backup schedule, not a test result, is what protects data — the test says whether a drive is fit to hold data today; the backup is for the drive that fails without notice tomorrow.

## Keeping watch without doing this by hand

The `smartmontools` package includes **smartd**, a background service
that polls every drive on a schedule, runs periodic self-tests, and
raises an alert when a counter moves. Its configuration lives in
`/etc/smartd.conf`. Setting it up belongs with monitoring and alerting,
in a later unit — the point here is that the manual check this unit
teaches is also available as a standing guard.

Re-run a long test before trusting a drive with a new role, after the
machine is physically moved, and on something like a yearly rhythm in
between. The **Disks** application shows a one-line assessment for
every drive whenever the quick answer is enough.

*Sources: Backblaze, "What SMART Stats Tell Us About Hard Drives"
(backblaze.com/blog/hard-drive-smart-stats), which names the five
attributes, the 76.7% figure, the position on attribute 187 and the
rate-of-increase qualifier; smartmontools documentation (smartctl(8),
smartmontools.org) for flag behaviour and self-test statuses. The
Seagate raw-value encodings — attributes 1, 7 and 195, and the
three-field packing of 188 — are community-documented (smartmontools
issue tracker and mailing list, TrueNAS and Unraid forums, the
Scrutiny project's issue tracker) rather than published by Seagate,
and are stated here with that weight. Checked 2026-08-09.*

*Correction, 2026-08-09: the first version of this unit listed all five
attributes as read-raw and flagged the Seagate packing trap only for
attributes 1, 7 and 195. It did not know that 188 is packed the same
way, so a reader following it would have decoded a raw value of 196611
as 196,611 timeouts rather than three. Found within a day, by the first
reader to meet a real Seagate 188 value.*
