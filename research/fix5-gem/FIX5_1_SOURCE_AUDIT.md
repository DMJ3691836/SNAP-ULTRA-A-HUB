# FIX5.1 — Evidence-ledger source audit (13 October 2026)

**Status: RESEARCH ONLY — NOT COMPILED, NOT REPLAY-VALIDATED, NOT FROZEN, NOT MERGED.**

This audit compares the merged FIX5 Parent/Bridge/Child research candidate with supplied SNAP indicator sources. The new FIX5.1 Pine file records only facts that FIX5 itself owns at ticket birth. It does **not** synthesize another indicator's labels from similar price action, award an A+ GEM, or change entry/stop/target/lifecycle rules.

## Baseline provenance and scope

- Prior branch merged to `main`: commit `0ade3550cfe107a8f7274f5122259505e0126649`.
- Existing candidate (untouched): `research/fix5-gem/SNAP_IFVG_LSQ_FIX5_GEM_RESEARCH.pine`.
- Prior frozen source SHA-256: `5869808bc37068c164571d30664d9b381a0623e8bddd8566aff4aede619147d7`.
- New parallel research file: `SNAP_IFVG_LSQ_FIX5_1_EVIDENCE_RESEARCH.pine`. Do not overwrite the previous candidate or source.

## Source findings and confirmed ownership

| Evidence / timeframe | Identified source indicator | Observed implemented signals or variables | FIX5 status |
|---|---|---|---|
| 1H+ Parent authority | FIX5 confirmed structural pivots; SNAP HTF Liquidity Map v1.0 separately has `buySideRaid`, `sellSideRaid` alerts | FIX5 `gemParentDir` is a confirmed previous-HTF pivot-break **proxy**; HTF Map raid event is independently supplied | Structural proxy implemented; HTF Map not connected |
| 15m Bridge navigation | FIX5 `gemBridgeDir`; LTS V2.0 prefreeze | LTS has separate breakout/trap, resistance/support trend trap, equal-high/low sweep and bullish/bearish BOS alerts | Bridge proxy implemented; no LTS provenance integrated |
| 15m liquidity / reclaim | SNAP Session Liquidity Hunt v2.1; TIMEbase Reclaim v2.0 | Liquidity Hunt: raid-armed/CISD/BUY/SELL confirmed. TIMEbase: range liquidity taken, manipulation/reclaim armed, reclaim entries, invalidation/target | No cross-indicator stage sequence mapped |
| 5m development | SNAP Pressure Map v1.3.1; SNAP Trend Flips v5.3 | Pressure Map confirms buy/sell transition, balance/absorption/exhaustion observations, and MTF pressure hierarchy; Trend Flips tracks sweep → rejection → MSS → flip, plus FVG/OB arrays | FIX5 samples 5m pivot-break direction; does not consume these events |
| 1m proof | SNIPPET v2.1b; SNAP Trend Flips v5.3 | SNIPPET focuses on NY 09:30–09:35 5m first-candle and 1m breakout/FVG/retest permission, not a universal 1m gate | FIX5 samples 1m pivot-break direction; does not consume first-candle or trend-flip proof |
| Native FIX5 LSQ / IFVG | FIX5 V6.4 multi-path engine | Own originating sweep, LSQ, displacement time, IFVG readiness, touch count, and Path A/B/D entry | Native evidence is now independently snapshotted in FIX5.1; no external GEM claim |

**Source status:** The external scripts were located in the user's prior uploaded/library files, **not** inside this GitHub repository. This is a *partial* cross-suite audit. An exact 15-model crosswalk requires gathering and version-pinning all final 15 source scripts; counts alone are not proof of interoperation.

## Critical gaps exposed

1. **No cross-script state transport.** A TradingView Pine indicator cannot normally read another indicator's internal mutable variables directly. Equivalent events must be exposed deliberately via compatible plots / `input.source` where supported, via a consolidated approved library, or via timestamped alert/webhook adapters outside Pine. None of these interfaces is validated here.
2. **Directional agreement is not event proof.** Confirmed 5m and 1m pivot breaks do not establish the ordered SNAP story MAP → RAID → RECLAIM → SHIFT → EXECUTE → CONFIRM → PAY, failed acceptance, EER/DEX participation, or A+ status.
3. **Lower-TF sampling is not an ordered ledger.** The merged `request.security(...,"5"/"1", f_gem_structure(...)[1])` samples one intrabar state, not every 1m/5m development within 15m. Realtime/historical results may diverge. Require `request.security_lower_tf()` array analysis or timestamped source events before sequential assertions.
4. **15m Bridge is a structural proxy.** It is derived from FIX5 pivots, not identical to LTS raid/trap/BOS labels.
5. **Path B has independent provenance risk.** The two Path B ticket births do **not** set `lastTradeLSQ`. The legacy value might come from a previous trade. The pre-existing webhook labels Path B LSQ `FAILED_PATH_INHERITED`, but this inheritance cannot be proven from these assignments alone. FIX5.1 therefore records **-1 (NOT VERIFIED)** for its *separate* native LSQ evidence field on B entries; native sweep timestamp is unspecified and only current B-reversal displacement time is captured. Legacy FIX5 fields are untouched pending fixture/replay validation.
6. **STOP HIT repetitions are not independent trades.** Multiple Bar Replay screenshots of one ticket/status are repeated observations, not a statistical count of distinct stop-outs. Group results by `activeSequenceId`/`lastTradeSequenceId` and exact entry time. Stop precedence on the same bar remains as in FIX5; OHLC screenshots do not establish intrabar stop/TP order.
7. **No A+ promotion.** A candidate's `gem_certified:false` stays false until independently verified NEXUS evidence and human approval. Publishing, broker execution and automated promotion remain OFF.

## FIX5.1 code change — native snapshot only

For **each of the six ticket births** (A long/short, B long/short, D long/short) the research candidate freezes additional fields at entry:

- `lastGemNativeLsqAtEntry`: own LSQ for A/D; `-1` unverified for B.
- `lastGemNativeSweepTimeAtEntry`: native sweep time for A/D; unknown for B.
- `lastGemNativeDispTimeAtEntry`: native displacement time for A/D; own reversal bar for B (not proof of predecessor).
- `lastGemNativeIFVGAtEntry`, `lastGemNativeTouchesAtEntry`: native A/D model observations; marked false/zero for B pending separate proof.
- `lastGemNativeEvidenceOrigin`: `FIX5_A_NATIVE_ONLY`, `FIX5_D_NATIVE_ONLY`, or `FIX5_B_REVERSAL_ONLY_PREDECESSOR_UNVERIFIED`.

Outputs: research Data Window plots and webhook fields `gem_evidence_origin`, `gem_playbook_mapping:"UNMAPPED"`, `gem_native_*`. **No** changes to six entry gates, price/stop/target calculations, ticket-state mutation, Path C inheritance, or automatic publication. These snapshots are observations, not an executable advantage score.

## Acceptance matrix before any merge to main

| Test | Acceptance evidence |
|---|---|
| Compile | Pine v6 compiles on TradingView 15m XAUUSD without error (NOT TESTED) |
| Default parity | With research Child gate OFF, every A/B/D entry, stop and TP at every tested bar matches merged FIX5 baseline (NOT TESTED) |
| Provenance | 2 each A/B/D; A/D native sweep/disp/LSQ captured; B separate LSQ = -1 (SOURCE CHECK ONLY) |
| Parent aligned | 1H bearish / 15m bearish / 5m & 1m bearish at short birth → class 1, still NEXUS pending (NOT REPLAYED) |
| Tactical Child | 1H bearish / 15m transitional / 5m & 1m bullish at long birth → class 2 reduced pending (NOT REPLAYED) |
| STOP precedence | Stop touched same bar as TP1 → STOP closes; sequence, frozen stop and snapshot preserved (NOT REPLAYED) |
| Path C | TP1 → full-body acceptance → runner retains original birth class/provenance/sequence (NOT REPLAYED) |
| Repainting / lower-TF | Compare historical and realtime lower-timeframe bar availability/last intrabar and event timestamps (NOT REPLAYED) |
| Bridge/source labels | Match exact LTS, Trend Flips, Session Hunt and Pressure Map bar timestamps rather than inferring from similar candle shapes (NOT WIRED) |

## Next engineering gate

Version-pin the remaining SNAP indicators and define a common event schema:
`{symbol, timeframe, event_time, closed_bar_time, source_id, source_version, source_sequence_id, side, stage, event_type, evidence_level, parent_relationship, invalidation_level, confirmed}`.

Map event *ownership*: 1H Parent and HTF raid; 15m Bridge and LTS/TIMEbase/CISD; 5m Child/Pressure/Trend Flip; 1m confirmed proof; FIX5 A/B/D tickets. Preserve chronology and contradictions, and require NEXUS/HUMAN APPROVAL to award A+ GEM. Keep Story Engine publishing human-gated.
