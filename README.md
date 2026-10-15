# SNAP ULTRA A+ HUB

SNAP ULTRA A+ HUB is a multi-layer TradingView Pine Script indicator that acts as a rule-based market-state classification and confluence engine.  It continuously converts raw chart data into named states, scores directional evidence, and communicates high-conviction A+ setups through visual labels, reference lines, a live dashboard, and machine-readable alerts.

---

## What it does

The indicator has four core responsibilities:

| # | Responsibility | What it observes / produces |
|---|---|---|
| 1 | **Observation** | ATR, dual EMAs, VWAP + bands, volume, RSI, swing pivots, rolling range |
| 2 | **Interpretation** | Trend/flow, MSS, premium/discount, BSL/SSL build-up, liquidity raids, displacement, FVG, VWAP alignment, DRT cycle |
| 3 | **Qualification** | DRT confluence score (max 15) or legacy 10-point score; A / A+ grade thresholds |
| 4 | **Communication** | Signal labels, ENTRY + MEAN REF lines, FVG boxes, sweep/pivot lines, dashboard, 17 alert conditions |

---

## Files

| File | Description |
|---|---|
| `SNAP_ULTRA_A_HUB_DEV_007.pine` | **Current release** — Pine Script v6, all features, execution mode |
| `SNAP-ULTRA-A-HUB.pine` | Earlier v5 baseline (kept for reference) |

---

## New in DEV 007

- **Pine Script v6** (upgraded from v5)
- **Execution Mode (Lightweight) toggle** — one switch suppresses all heavy drawings while keeping signal calculations and A+ labels live
- **Corrected signal labels** — entry price line is now `ENTRY` (was `SWEEP`); mean reference line is `MEAN REF` (was `OB REF`)
- **DRT Cycle Model** — day-open level capture → intraday raid detection → post-raid displacement tracking → DRT FVG memory → retest scoring → DRT A+ signal
- **Optimised default inputs** pre-applied (see table below)
- **Dashboard** shows active mode (DRT MODEL / LEGACY SCORE) and Execution Mode status
- **Drawing object caps** reduced for better chart performance

---

## Execution Mode

Enable **Execution Mode (Lightweight)** in the `⚡ Execution Mode` input group when trading live to reduce chart overhead.

**Suppressed in Execution Mode (no permanent settings change):**
- FVG reference boxes (structure + DRT)
- DRT inefficiency zone boxes
- Premium/Discount zone boxes
- VWAP deviation bands
- Sweep logic lines
- Exit/stop logic lines
- Pivot reference lines and labels
- DRT opening-level lines
- Dashboard table

**Always active regardless of mode:**
- Core signal calculations (BUY/SELL A+ logic unchanged)
- A+ BUY / SELL plotshape triangles
- A+ BUY / SELL score labels
- ENTRY and MEAN REF reference lines
- Kill-zone background shading
- Fast/Slow EMA and VWAP plots
- All alert conditions

---

## Optimised default inputs (DEV 007)

| Parameter | DEV 007 default | Previous default | Why changed |
|---|---|---|---|
| `drtTriggerScore` | 11 | 10 | Fewer low-quality DRT signals |
| `drtRaidMemoryBars` | 90 | 120 | Avoids stale raid context |
| `drtFvgMemoryBars` | 90 | 120 | Avoids stale FVG context |
| `drtLevelTolAtr` | 0.15 | 0.20 | Tighter level alignment |
| `drtRetestProxAtr` | 0.25 | 0.35 | Cleaner retest qualification |
| `drtRetestCooldown` | 20 | 12 | No duplicate retest prints |
| `displacementAtr` | 0.65 | 0.55 | Higher impulse quality bar |
| `fvgMemoryBars` | 60 | 80 | Older FVGs less tradeable |
| `vwapBandMult` | 1.75 | 2.00 | Earlier band reaction |
| `highVolMult` | 1.3 | 1.5 | Usable in quieter sessions |
| `deltaThreshold` | 0.12 | 0.10 | Reduces flow noise |
| `signalCooldownBars` | 20 | 15 | Less signal clustering |
| `maxSweepLines` | 50 | 80 | Reduced drawing objects |
| `maxExitStopLines` | 80 | 120 | Reduced drawing objects |
| `maxPivotRefs` | 8 | 12 | Reduced drawing objects |

---

## Quick presets

### Preset A — Conservative (higher win-rate, fewer trades)
```
drtTriggerScore      = 12
displacementAtr      = 0.70
drtLevelTolAtr       = 0.10
drtRetestProxAtr     = 0.20
signalCooldownBars   = 25
```

### Preset B — Balanced (recommended baseline)
Use the DEV 007 defaults from the table above.

### Preset C — Aggressive (more signals)
```
drtTriggerScore      = 9
displacementAtr      = 0.50
drtLevelTolAtr       = 0.25
drtRetestProxAtr     = 0.40
signalCooldownBars   = 10
```

---

## Installation

1. Open TradingView Pine Script Editor.
2. Paste the contents of `SNAP_ULTRA_A_HUB_DEV_007.pine`.
3. Click **Save** then **Add to chart**.
4. Adjust session times in the **Sessions / Kill Zones** group to match your broker's server timezone.
5. For live execution, enable **Execution Mode (Lightweight)** in the `⚡ Execution Mode` group.

---

## Alerts

Configure alerts via the TradingView Alerts dialog.  Available conditions include:

- `A+ BUY Signal` / `A+ SELL Signal` — main trading signals
- `DRT SSL Raid (Bullish)` / `DRT BSL Raid (Bearish)` — DRT raid detection
- `DRT A+ BUY Core` / `DRT A+ SELL Core` — DRT threshold reached (pre-signal)
- `SSL Raided` / `BSL Raided` — standard liquidity sweeps
- `Bullish / Bearish MSS` — market structure shift
- `Bullish / Bearish Displacement` — impulse candle
- `Bullish / Bearish FVG Created` — fair value gap formed
- `Bullish / Bearish VWAP Cross` — VWAP level crossed
- `A+ Grade (Legacy)` — A+ reached on legacy score path

---

*SNAP ULTRA A+ HUB is for educational and informational purposes. It is not financial advice.*
