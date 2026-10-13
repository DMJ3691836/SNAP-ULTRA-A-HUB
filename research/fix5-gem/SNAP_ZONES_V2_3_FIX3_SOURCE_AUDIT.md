# SNAP Zones v2.3 FIX3 — Session and Liquidity Reference Source Audit

13 October 2026. STATUS: SOURCE REVIEWED, NOT COMPILED OR BAR-REPLAY VALIDATED. No changes to executable scripts or FIX5 trade rules.

SOURCE: Uploaded "Pasted markdown(20261013-194939).md", SHA-256 7171c1ebff2d0de0487ab34265eaae7bcd894f8cf25996c817a4578a871d1050; 23,819 bytes, 905 text lines. Big-paste source includes Markdown formatting wrappers and HTML nonbreaking-space entities: NOT directly compiler-ready as pasted.

## Confirmed capabilities (from supplied source)

- Default timezone America/New_York; market windows: Sydney 17:00-19:00, Tokyo 19:00-00:00, London 02:00-05:00, New York 08:00-11:00; dedicated US Open 09:30-10:30. These are configured chart windows, not a claim of full market hours.
- Climax WINDOWS: London 04:00-05:00; NY 10:00-11:00. These are time windows, NOT confirmed participation climax signals.
- Silver Bullet windows: London 03:00-04:00, AM 10:00-11:00, PM 14:00-15:00. Optional bullish/bearish 3-candle FVG zones within configured windows; FVG location is not entry permission.
- The generic session function draws dynamically updated H/L, midpoint and session box, optionally extends completed session high/low as dashed lines. Active H/L variables reset at session end. The completed data is visible in chart objects, NOT independently exported as a persistent named session time series.
- Right-side current-reference lines and labels: Daily Open, PDH/PDL, PWH/PWL, ADR High/Low. Previous day/week references request confirmed bars via [1] offsets; ADR uses average of prior completed daily ranges. Note ADR High/Low are drawn at Daily Open +/- ADR, a 2*ADR full span; treat these as projection levels, not a verified daily range.
- Local Liquidity Sweep BOS module defaults to 15m and below; BSL high sweep with close back inside arms a bearish candidate and freezes the last minor low, SSL low sweep arms bullish and freezes the last minor high. Later confirmed close through stored level within 30 chart bars completes bearish/bullish BOS. Four alertcondition events: BSL Sweep, SSL Sweep, Bearish BOS, Bullish BOS.

## What the script does NOT yet calculate

SNAP Zones maps session reference geometry that enables session-to-session interpretation but does not compute distinct machine-readable handoff states. No explicit confirmed sequence for "Asia High Raid -> London Failed Acceptance", "London Low Reclaim -> NY Inside Value", or "NY Acceptance Above London High" exists in this uploaded source. Drawing ranges or extending levels is not the same as stateful session acceptance/continuation/failed acceptance.

It likewise does not certify 1H Parent Authority, 15m AMD Bridge, 5m Trend Flip, EER/DEX participation, GEM A+ status, or FIX5 ticket fills. The 15 M-01..M-15 playbook models can overlap around these session events but are not themselves 15 indicators.

## Important technical source caveats

1. High/low sweep acceptance is not explicitly gated by barstate.isconfirmed; sweep labels and alerts may be provisional intrabar. BOS itself requires barstate.isconfirmed. Validate alerts with Once Per Bar Close and candle replay.
2. The showBos switch is part of sweep detection, not purely visual; switching off prevents local sweep/BOS events and corresponding alerts.
3. maxBarsAfterSweep counts chart bars; 30 bars means different elapsed time on 1m, 5m, and 15m.
4. Silver Bullet FVG box.new calls do not register with the generic session object-retention arrays; inspect display limits and GC effects during long histories.
5. Active session state high/low resets when the session ends; historical right-side reference objects reflect the currently evaluated bar, not automatically an immutable prior timestamp. True source-native session ID/high/low snapshots are needed for auditable cross-session mapping.
6. New York clock windows are configurable and DST-aware via timezone; verify instrument and exchange feed alignment when comparing sessions.
7. The current Daily Open requested with lookahead_on is a known day-open anchor, unlike an unconfirmed daily high; prior-day/week levels are offset. Still validate historical chart/timeframe context.

## Correct owner mapping for the SNAP Story

- MAP: SNAP Zones session time, named session boundaries, developed and completed H/L/mid, prior-day/week references and Silver Bullet time windows.
- RAID: local BSL/SSL sweep candidate from Zones (bar-close confirmation required), plus independent verified Liquidity Hunt/4H Manip events.
- RECLAIM and acceptance: must be explicitly reconstructed using frozen cross-session references and confirmed bars, or derived from separately versioned TIMEbase / Liquidity Hunt / CISD source events.
- SHIFT: Zones subsequent confirmed minor BOS supports local shift; AMD 15m / Trend Flips 5m identify their own higher-proof states.
- EXECUTE, CONFIRM, PAY: remain FIX5/NEXUS execution/ticket and human-approved Story responsibilities.

## Proposed integration contract — NOT emitted currently

Proposed producer events: snap_zones.session_started; snap_zones.session_completed {session_id, tz, start/end, high, low, midpoint}; snap_zones.reference_level {kind, effective_time, level}; snap_zones.bsl_sweep and ssl_sweep {sweep_id, bar_close_time, reference, confirmed_close}; snap_zones.bear_bos and bull_bos {sweep_id, frozen_bos_level, bar_close_time}. NEXUS, not current SNAP Zones, would derive cross_session_relation {from_session_id, to_session_id, level, raid, acceptance, reclaim, continuation, evidence_timestamp}.

All event names above except the four existing alertcondition labels are proposal only, not claimed source outputs. Do not grant A+ GEM privilege or modify live ticket state based on session geometry alone. Keep the Story Engine human-approved, never auto-published.

## Disposition

SNAP Zones v2.3 FIX3 is SOURCE REVIEWED and MUST REMAIN IN THE SNAP SUITE as the session/location reference layer. This removes it from the source-inspection queue, not from the chart or strategy. Keep FIX5.1 PR #4 as draft until producer adapters, TradingView compilation and Bar Replay are verified.
