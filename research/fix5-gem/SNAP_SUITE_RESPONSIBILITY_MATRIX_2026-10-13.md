# SNAP Indicator Responsibility Matrix
**Forward-test source review baseline | 2026-10-13**

**Scope: 12 core analytical layers + 5 companion overlays; governance and archived research separate.** This is the approved analytical inventory for research, not proof that all components have been wired or TradingView-replay-tested.

## A. Core Analytical Layers (12)

| ID | Indicator | Operating layer | Primary source responsibility |
|---|---|---|---|
| 01 | SNAP HTF Liquidity Map | W / D / 4H / 1H | Parent territory, protected structural context and higher-timeframe liquidity |
| 02 | Bullish Event Horizon | 1H -> lower TF | Bullish territory and lower-timeframe sweep/reclaim permission |
| 03 | Wyckoff Territory Structure | Multi-TF | Auction phase, accumulation/distribution and territory |
| 04 | AMD Trend Bias v2.1 | 15m | Main BOS, protected high/low, Fib retracement, frozen Mini BOS, later BUY/SELL trigger |
| 05 | SNAP Pressure Map v1.3.1 | Multi-TF | Directional participation, pressure, weakening/absorption-test and handoff evidence |
| 06 | LTS v2.0 | Multi-TF | Liquidity-trap POIs, failed breaks, sweeps, structural reactions |
| 07 | SNAP Session Liquidity Hunt v2.1 | Intraday | RAID, CISD, origin OB/mitigation and post-raid evidence |
| 08 | IFVG/LSQ FIX5 + FIX5.1 research | 15m/GEM | Native LSQ/sweep/displacement/IFVG, A/B/C/D model paths, ticket and pending GEM telemetry |
| 09 | TIMEbase Liquidity v2.0 | Intraday/LTF | Time-defined liquidity ranges, reclaim and execution geometry |
| 10 | Brooks Price Action Pro | Execution TF | Pullback, breakout/range failure and candle proof quality |
| 11 | 9AM Playbook 2.3a | NY morning/LTF | Morning sweep, BOS/IFVG, POI retest and precise setup |
| 12 | Five-Step + VSA | Intraday | Failed breakout/reclaim and price/volume-spread confirmation |

## B. Companion Overlays (5)

| ID | Indicator | Operating layer | Distinct source responsibility |
|---|---|---|---|
| C1 | SNAP Trend Flips v5.3 | 1H origin -> 5m | Frozen 1H OB/FVG array location; 5m sweep -> A+ rejection -> MSS -> Trend Flip |
| C2 | SNAP Zones v2.3 FIX3 | Sessions | Sydney/Tokyo/London/NY session H/L/midpoints, opening windows, daily/weekly references, local sweep/BOS |
| C3 | SNAP Macro Interval Zones v1.2 | Four NY time windows | POST-observation BULL/BEAR EXPANSION/REACTION/BALANCED and rolling reaction frequencies |
| C4 | 4H Manipulation + Stateful CISD v2.0 | Closed 4H -> chart LTF | 4H liquidity raid/failed acceptance; freeze opposing-candle OPEN, later confirmed CISD |
| C5 | SNIPPET v2.1b | 5m -> 1m | NY first-candle model, session-specific breakout, FVG/retest and 1m entry permission |

## C. Not included in mandatory active suite

**SNAP HTF_LTF v1.8 / SNAP RANGE v1.8 — Adaptive Range Context:** Archive intact. Optional W/D/4H range-quartile, HTF liquidity/imbalance and Sunday–Monday deviation research only. Do not count as a mandatory eighteenth analytical component. Do not treat its simple "BUY-SIDE CONTROL" / "SELL-SIDE CONTROL" dashboard proxy as verified persistent Parent authority. See `SNAP_RANGE_V1_8_SOURCE_AUDIT.md`.

## D. System and governance (excluded from indicator count)

- **Webhook Signal Climax:** event/alert transport, not trade or GEM approval.
- **FIX5 ticket engine:** sole source of truth for its own A/B/D entry ticket births, sequence, stop, TP1, TP2/runner state; Path C is *same ticket*, not another trade.
- **NEXUS:** timestamped cross-indicator evidence aggregation, Parent/Bridge/Child classification, contradictory-state preservation, privilege checks.
- **15 GEM auction playbook models (M-01..M-15):** descriptive and potentially overlapping auction patterns, **not** 15 indicators. P-06 tactical Child privilege is not M-06 auction-pattern label.
- **Story Engine:** MAP -> RAID -> RECLAIM -> SHIFT -> EXECUTE -> CONFIRM -> PAY, with EER/DEX as supporting evidence inside stages. CHART -> INDICATOR DATA -> STORY ENGINE -> TELEGRAM DRAFT -> HUMAN APPROVAL -> PUBLISH. Forward test NEVER auto-publishes.
- **Privileges:** FULL PARENT (resolved + aligned + verified); REDUCED TACTICAL CHILD (qualified independent Child without higher-timeframe promotion); NONE/PENDING (proof incomplete).

## Frozen technical doctrine

**1H Parent authority -> 15m Bridge and POI -> 5m Child development -> 1m execution proof.** A 4H sweep may supply higher-timeframe location, but does not by itself transfer the 1H Parent regime. An observed source event must be distinguishable from an inference or a later confirmation. Same auction, different resolution; correlated candles must not be double-counted as independent votes.

## Validation status

- **Source-level role review:** mapped (selected source versions; complete 17-script version lock still to be verified).
- **FIX5 Parent/Child merged research:** preserved on `main`; NOT production/forward-test certified.
- **FIX5.1 native evidence research:** separate Pine candidate in draft PR #4, NOT merged/compiled/replay-certified.
- **Cross-script NEXUS connectors, standalone A+ award, real fills:** NOT implemented/approved by this matrix.
- **SNAP RANGE active chart:** excluded (optional archived research).
