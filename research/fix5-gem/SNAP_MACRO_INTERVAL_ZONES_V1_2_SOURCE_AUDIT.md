# SNAP Macro Interval Zones v1.2 — reaction statistics evidence audit

**Reviewed 13 Oct 2026 — source-level only; not TradingView-compiled, forward-replayed, or NEXUS-integrated.** This is the narrower *reaction-timing companion* to SNAP Zones v2.3 FIX3. It is NOT the separate economic-calendar SNAP Macro provider, and the name "Macro" does NOT prove that any economic announcement occurred.

## Source and version

- Supplied pasted source: `Pasted markdown(20261013-195233).md`, SHA-256 `64454e0faa7b5831f8ba4b0058c7c3d5a31c0abd593ab19ece3d2b3e54d6a3ce`, 19,195 bytes, 655 filesystem lines.
- Native preserved Library script: `SNAP_Macro_Interval_Zones_v1.2_Reaction_Statistics_FIXED.pine` (16,544 bytes). On whitespace-insensitive source comparison, after decoding pasted Markdown bold wrappers, HTML entities and escaped `*`/`<`/`>`, **286 of 286 nonblank source lines matched**. Do not use the formatted pasted attachment directly as executable Pine.
- Current v1.2 configured New York windows: Zone 1 **09:50–10:10**, Zone 2 **10:50–11:10**, Zone 3 **13:50–14:10**, Zone 4 **02:50–03:50**. Note older discussion had described Zone 4 as 02:50–03:10; this source specifies an hour. Do not silently collapse them.

## Actual state and classification

- Weekday toggles Monday–Friday, timezone `America/New_York`.
- Configured defaults: PRE 20 minutes; ACTIVE the named window; POST 30 minutes; ATR 14; expansion threshold 0.75 ATR; directional threshold 0.20 ATR; rolling 20 observations per zone.
- `zOpen,zHigh,zLow,zAtr,zActive,zCompleted,zDateKey` are four-zone arrays; active bar interactions accumulate the zone H/L. A completion check when the bar *contains* POST-end calls `f_reaction_text`, pushes a statistic and draws BULL/BEAR EXPANSION or REACTION or BALANCED.
- Direction is from `postClose - zoneOpen`; an EXPANSION label is chosen if **either the ACTIVE zone's high–low range OR net movement to the POST-end sampled bar's close** meets the expansion threshold, with net direction meeting 0.20 ATR. Therefore **BULL EXPANSION does not prove persistent one-direction bullish delivery, confirmed acceptance, or a structural SHIFT**. It may accompany substantial two-way volatility.
- Rolling table shows N, percentages bullish/bearish/other, and mean excursion. The excursion is `max(abs(activeHigh-zoneOpen),abs(activeLow-zoneOpen))/atrAtZoneStart`, measured within ACTIVE window. It is NOT a confirmed trade's MFE, realized R, expectancy or causal conditional probability of a successful entry.
- Four event/label categories? Exactly five outcomes: `BULL EXPANSION`, `BEAR EXPANSION`, `BULL REACTION`, `BEAR REACTION`, `BALANCED`. Bull/BEAR counts combine expansion and reaction into their respective directions.
- This version displays boundaries, shading, completion labels, and a statistics table; **there are no alertcondition()/alert() webhook event emitters** for outcomes in this supplied source. NEXUS must not claim they are already fed into its event ledger.

## Implementation caveats for forward testing

1. `completeNow` is based on a bar that contains the POST-end timestamp, not `barstate.isconfirmed`. It reads that bar's current `close` and can be provisional in realtime. On 15m, 5m or 1m, the *effective observation/confirmation timestamp* can differ. Require closed-bar evidence and store `sampled_bar_close_ms`.
2. The actual outcome is **unknown at zone open**. Do not leak retrospective `BULL EXPANSION` or `BEAR EXPANSION` into prior FIX5 or GEM entry snapshots. Record a pre-entry zone-state `PRE/ACTIVE/POST/PENDING`; attach reaction **only when earned**, usually as CONFIRM/Result or as context for a *later* trade.
3. `zDateKey` resets daily and rolling statistics persist across recent observations. This is aggregate behaviour, not a charting trade ledger keyed by FIX5 sequence ID.
4. OHLC intervals can overlap zones on coarser timeframes. `f_in_window` counts any intersecting bar; active-range measurements can include prices outside exact boundary timestamps. Test 1m, 5m and 15m separately.
5. Historical plots and table contents need careful replay comparisons. The script does not verify economic release events or news-surprise calculations.
6. The Zone 4 configuration defaults to 02:50–03:50, distinct from earlier 02:50–03:10 description; confirm which interval is intended before adjusting source.

## Historical examples recovered from archive

- **2 September 2026, XAUUSD**, historical Telegram review: first 04:50 NY long entered 4310.79, stopped 06:00 (reported -1R); second 06:00 long 4316.04 targeted 4371.95 (reported +6.49R). Its narrative **explicitly names SNAP Macro Zones** for broader liquidity destination/upper expansion area and SNAP Zones for session references. This does NOT establish that v1.2's specific BULL EXPANSION label was generated on any given candle.
- **24 September 2026, XAUUSD**, historical Telegram review: long at **13:50 NY**, entry 4260.22, stop 4256.07, target 4282.49 (reported +5.36R, target 21:00 NY). Entry is at Zone 3 start. Archived report mentions **session timing** and auction RAID→RECLAIM→SHIFT, but not a verified v1.2 outcome label. Its POST-end is 14:40 NY, with actual sampled bar-close possibly later; therefore NO Zone 3 expansion outcome was knowable at the 13:50 entry.
- Earlier **19 July 2026** discussion treated Macro Intervals as a *timing amplifier after* structural/location/confirmation prerequisites; it did not establish a source-certified trade entry.

These are research examples reported in historical posts, NOT audited broker fills and NOT retrospectively certified A+ GEM executions.

## Pairing with SNAP Zones and GEM doctrine

SNAP Zones = broad sessions and H/L/midpoint, named intraday liquidity, current daily/week/ADR references, local sweep/BOS.

SNAP Macro Interval Zones = narrower time windows, ACTIVE-zone price range, **later** POST-period reaction and rolling conditional sample descriptions.

AMD = 15m Bridge structure and frozen invalidation. Trend Flips = 1H OB/FVG source array plus 5m Child sweep/rejection/MSS. FIX5 = LSQ/IFVG execution ticket sequence and frozen entry data. EER/DEX = participation-vs-Result evidence, not a direction oracle.

NEXUS should record `{tickerid, source_version, zone_id, zone_start/end_ny, pre_start, post_end, bar_close_time, zone_open/high/low, atr_ref, net_move, zone_range, reaction_class, completion_observed_at, parent_dir, bridge_state, child_state, ticket_id_if_any, evidence_purpose}`. This is a **PROPOSED** adapter contract, NOT currently emitted by this indicator. When recording source-derived classifications, distinguish PENDING from REACTION_CONFIRMED and prevent later outcomes from overwriting entry-time GEM class or privilege. Never double-score a reaction label and a structural displacement derived from the same underlying candles as independent votes.

**Disposition:** SOURCE REVIEWED, retain both SNAP Zones and Macro Interval Zones. Preserve current code. Keep FIX5.1 GitHub PR #4 draft until compiler, replay, event-adapter and NEXUS validation; Story Engine remains human approved.
