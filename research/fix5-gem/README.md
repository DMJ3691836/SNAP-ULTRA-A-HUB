# FIX5 / SNAP A+ GEM — Parent and Child Research Integration

## Scope and provenance

- **Source**: `SNAP_IFVG_LSQ_FIX5_FROZEN_BASELINE.pine`, SHA-256 `5869808bc37068c164571d30664d9b381a0623e8bddd8566aff4aede619147d7`; the 13 October paste has the same nonblank source lines.
- **Working indicator**: `SNAP_IFVG_LSQ_FIX5_GEM_RESEARCH.pine`. This is a separate **research candidate**, not a replacement for the frozen baseline.
- **Not yet TradingView compiled or candle-replay verified**. Source checks are static and do not certify A+, actual trade fills, entry timing or live safety.

## Behaviour

1. **Parent (1H+)** uses persistent confirmed HTF pivot break direction. An unchanged bearish Parent stays bearish through a bullish tactical Child bounce. Parent state is read from the previous closed HTF candle.
2. **15-minute Bridge** uses the existing 15-minute confirmed swing references to retain its structural direction. `ALIGNED` requires Parent, Bridge and entry side to match. If Parent agrees but the 15m Bridge is opposite it displays `CONTRADICTORY`; other mismatches remain `TRANSITIONAL`.
3. **5-minute / 1-minute Child** observe confirmed pivot-break structural states separately. Both must agree with entry side before a candidate gains class 1 or class 2. Without agreement the class is `CHILD PROOF PENDING`.
4. **Candidate codes**: `0 = CHILD PROOF PENDING`, `1 = PARENT-ALIGNED CANDIDATE`, `2 = TACTICAL CHILD CANDIDATE` (Parent unresolved/opposite or Bridge not aligned).
5. **Privilege** is always marked **PENDING NEXUS**: `FULL - PENDING NEXUS` or `REDUCED - PENDING NEXUS`. FIX5 alone cannot assert the RAID/failed-acceptance/RECLAIM/SHIFT/EER/PAY chain or automatically award A+ GEM.
6. **A/B/D execution paths** are independent from GEM class. All six new-ticket births freeze the authority context with the original sequence ID. **Path C** remains the same trade, inherits its original snapshot, and is never a fresh Parent/Child candidate.
7. **Default: OBSERVE ONLY**. Optional `RESEARCH ONLY: require 5m + 1m structural proof before FIX5 entry` is OFF. Turning it on may filter entries; only do this in a **15-minute chart** after replay and baseline comparisons. All original entry thresholds, stop/target geometry and lifecycle handling are left unchanged.
8. Entry snapshot is included on additional ticket rows, Data Window plots and webhook JSON. A trailing `gem_certified:false` explicitly blocks consumers from mistaking the Pine candidate for a NEXUS-approved GEM.

## Critical limitation

TradingView's `request.security()` lower-timeframe sampling can differ between historical and realtime execution. For 15-minute evaluation the 5m/1m request samples the last lower-timeframe result with `[1]` on the underlying series to exclude its developing bar. This is **research-grade**, not a verified intrabar event reconstruction. True rigorous sequence proof requires timestamped lower-timeframe events or `request.security_lower_tf()` arrays and NEXUS evidence, which are outside this safe baseline patch.

## Required 15m Bar Replay acceptance matrix

| Scenario | Expected GEM snapshot at new valid A/B/D entry | Ticket invariant |
|---|---|---|
| Parent bearish; Bridge transitional; Child bullish 5m/1m proven | `TACTICAL CHILD CANDIDATE`; reduced privilege **pending NEXUS** | Same ticket ID through TP1/runner and subsequent Parent changes |
| Parent bullish; Bridge bullish; Child bullish 5m/1m proven | `PARENT-ALIGNED CANDIDATE`; full privilege **pending NEXUS** | No automatic upgrading of older tactical tickets |
| Parent bullish; Bridge bearish; Child bullish | `TACTICAL CHILD CANDIDATE`, `CONTRADICTORY` Bridge | No `PARENT` misclassification |
| Child only has 5m bullish and 1m unresolved | `CHILD PROOF PENDING`; no privilege | Default FIX5 path A/B/D remains executable, research gate ON must withhold new entry |
| Opposite liquidity sweep during an ACTIVE/TP1/RUNNER ticket | New observation only | Frozen original stop/targets, ID, snapshot; stop precedence unchanged |
| Path C accepted TP1 extension | Original class snapshot carried forward | No new ticket and no fresh GEM snapshot |
| After CLOSED a new valid entry forms | New snapshot from then-current hierarchy | Different sequence ID |

Run static checks locally: `python -m unittest discover -s tests -v`. This does **not** replace past FIX5 replay/compile checks. Keep publishing / broker execution **OFF** for the research candidate.
