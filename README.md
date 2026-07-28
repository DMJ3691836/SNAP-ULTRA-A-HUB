# SNAP ULTRA A+ HUB

**SNAP ULTRA A+ HUB** is a rule-based market-state classification and confluence engine built in Pine Script v5 for TradingView.

It continuously converts raw chart information into higher-level states and grades them through a transparent 10-point scoring system so that only the highest-confluence setups produce a signal.

---

## How it works

The HUB has four responsibilities:

### 1 · Observation
Monitors the market across multiple dimensions every bar:

| Dimension | What is measured |
|-----------|-----------------|
| Structure | Swing highs/lows → HH, HL, LH, LL |
| Range | Rolling session high/low and midpoint (premium/discount boundary) |
| Liquidity | Equal highs (BSL) and equal lows (SSL) |
| Momentum | Fast and slow EMA position and slope |
| Value | VWAP alignment |
| Volume | Volume relative to 20-bar average |
| Volatility | 14-bar ATR used for displacement sizing |

### 2 · Interpretation
Converts raw price behaviour into named market states:

| Market State | Detection logic |
|---|---|
| **Building liquidity** | Two swing levels within the equal-level tolerance |
| **Raiding buy-side liquidity** | Wick above last swing high; close below it |
| **Raiding sell-side liquidity** | Wick below last swing low; close above it |
| **Trading in premium** | Close above the rolling range midpoint |
| **Trading in discount** | Close below the rolling range midpoint |
| **Shifting bullish structure (MSS ↑)** | Close crosses above the last confirmed swing high |
| **Shifting bearish structure (MSS ↓)** | Close crosses below the last confirmed swing low |
| **Displacing away from a level** | Candle body ≥ ATR × multiplier with above-average volume |
| **Creating a fair value gap** | Three-candle imbalance (gap between bar 0 and bar 2) |
| **Retracing into an imbalance** | Close inside the most-recent FVG boundary |
| **Aligning with VWAP** | Close above (bull) or below (bear) session VWAP |
| **Confirming with EMA & flow** | Fast EMA above/below slow EMA and expanding in trend direction |

### 3 · Qualification (Scoring)
Each bullish or bearish condition contributes **1 point** toward a directional score (maximum **10**).

| Point | Bullish condition | Bearish condition |
|-------|-------------------|-------------------|
| 1 | EMA trend (bull) | EMA trend (bear) |
| 2 | EMA flow expanding | EMA flow expanding |
| 3 | In discount zone | In premium zone |
| 4 | SSL raided | BSL raided |
| 5 | Bullish MSS | Bearish MSS |
| 6 | Bullish displacement | Bearish displacement |
| 7 | Retracing into bullish FVG | Retracing into bearish FVG |
| 8 | Price above VWAP | Price below VWAP |
| 9 | Higher low (HL) | Lower high (LH) |
| 10 | High volume | High volume |

| Grade | Threshold (default) | Meaning |
|-------|---------------------|---------|
| **A** | ≥ 7 / 10 | High confluence – monitor closely |
| **A+** | ≥ 9 / 10 | Highest confluence |
| **Trigger** | A+ **and** displacement | Entry-ready signal |

### 4 · Communication
The HUB communicates through five output channels:

| Channel | Content |
|---------|---------|
| **Labels** | HH / HL / LH / LL structure; RAID ↑ / ↓; MSS ↑ / ↓; A / A+ grade on first qualifying bar |
| **Zones** | Semi-transparent premium (red) and discount (teal) boxes over the rolling range |
| **Boxes** | Fair value gaps – teal for bullish, red for bearish |
| **Lines** | Dashed orange lines at the last confirmed BSL and SSL levels |
| **Dashboard** | Live top-right table showing every market state, the directional score, grade, and current signal |
| **Alerts** | 15 named `alertcondition` conditions (see below) |

---

## Alert Conditions

| Name | Fires when |
|------|-----------|
| A+ Long Trigger | A+ bull score **and** bullish displacement |
| A+ Short Trigger | A+ bear score **and** bearish displacement |
| Sell-Side Liquidity Raided | SSL sweep detected |
| Buy-Side Liquidity Raided | BSL sweep detected |
| Bullish Market Structure Shift | Close crosses above last swing high |
| Bearish Market Structure Shift | Close crosses below last swing low |
| Bullish Displacement | Large bullish body with above-average volume |
| Bearish Displacement | Large bearish body with above-average volume |
| Bullish FVG Created | Bullish 3-candle imbalance formed |
| Bearish FVG Created | Bearish 3-candle imbalance formed |
| Building Liquidity | Equal highs or equal lows detected |
| Bullish VWAP Cross | Close crosses above VWAP |
| Bearish VWAP Cross | Close crosses below VWAP |
| A+ Grade Signal | Score reaches A+ threshold |
| A Grade Signal | Score reaches A threshold |

---

## Settings

| Group | Setting | Default | Description |
|-------|---------|---------|-------------|
| Structure | Swing Length | 10 | Bars on each side of a pivot |
| Liquidity | Equal-Level Tolerance (%) | 0.02 % | Max price distance for equal levels |
| Liquidity | Range Look-back (bars) | 50 | Rolling range period |
| Momentum & Value | Fast EMA | 20 | |
| Momentum & Value | Slow EMA | 50 | |
| Momentum & Value | Use VWAP | true | Include VWAP in scoring |
| Displacement | ATR Multiplier | 1.5 | Body size relative to ATR |
| Scoring | A Score Threshold | 7 | Minimum score for grade A |
| Scoring | A+ Score Threshold | 9 | Minimum score for grade A+ |
| Display | Show Fair Value Gaps | true | |
| Display | Show Liquidity Level Lines | true | |
| Display | Show Structure Labels | true | |
| Display | Show Dashboard | true | |
| Display | Show Premium / Discount Zones | true | |
| Display | Show A / A+ Grade Labels | true | |

---

## Installation

1. Open [TradingView](https://www.tradingview.com) and navigate to the Pine Script editor (`/pine`).
2. Paste the contents of `SNAP-ULTRA-A-HUB.pine` into the editor.
3. Click **Add to chart**.
4. Adjust settings under the indicator's ⚙ menu.
5. Set up alerts via the 🔔 Alert dialog using any of the named alert conditions.

---

## License

Apache License 2.0 – see [LICENSE](LICENSE).
