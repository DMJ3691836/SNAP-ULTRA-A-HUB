# FIX5.1 — AMD Trend Bias v2.1 + SNAP Trend Flips v5.3 source audit

**Status:** source-level review, 13 Oct 2026. Research-only. No TradingView compilation/replay verification. Preserve frozen FIX5 and all external indicator sources unchanged.

## Input provenance

- AMD Trend Bias v2.1 - Clean Structure: user-uploaded generated paste `Pasted markdown(20261013-185817).md`, original pasted representation, SHA-256 `0d3744cdce6ee6e2137fc5976870a500146b15fdae6e5c71c6b5a0287fa1e060` (27,090 bytes, 917 text lines). The upload contains Markdown bold wrappers and HTML space entities; it **is not** an install-ready `.pine` file. Read its Pine *semantics*, do not publish raw pasted text as executable code.
- SNAP Trend Flips v5.3 Stateful Clean Structure (**Readable Zones**) source: library file `SNAP_Trend_Flips_v5.3_Stateful_Clean_Structure_READABLE_ZONES.pine`, SHA-256 `09f6f5414961fd157d61634d06d396105b2a502a44c9b6c1dbb17f5c3567c686` (49,416 bytes, 2,650 lines). There is a distinct `COMPLETE.pine` revision, hash `9fcd6c3ec20a03d7c3ef8b8e8a3de50d51f2741197c488b700f78ca6e09e7c79`; **do not silently swap versions**.
- SNIPPET v2.1b previously inspected and narrowly session-specific; its 09:30–09:35 5m opening location and 1m permission logic are not a universal replacement for other 1m confirmation engines.
- **No raw copies of these external indicator sources are published in this public repo by this audit.** Audit results and proposed event contracts only.

## AMD Trend Bias v2.1 — actual source behaviour

Strictly **15-minute** architecture: `is15m = timeframe.isminutes and timeframe.multiplier == 15`; this script does **not** calculate independent 1H Parent direction.

1. Main `lastMainLow`/`lastMainHigh` pivot break (default pivot 3; optional close requirement) creates `newBearishMainBreak` / `newBullishMainBreak`.
2. Store `bearBiasActive` / `bullBiasActive`, LBOS, `bearProtectedHigh` / `bullProtectedLow`, prior external swing as target, Fib 25/50/75%, reset opposite bias.
3. Require qualifying primary retracement (`bearPrimaryTouch`/`bullPrimaryTouch`; default 25%) and freeze mini BOS pivot; `miniBearBreak` / `miniBullBreak` must be on a **later** bar; optional close-based mini break and tick buffer.
4. After mini BOS, `bearishTrigger` / `bullishTrigger` requires a **later** retracement into Fib band or preferred 50%; `AMD SELL` / `AMD BUY` marks completion of the 15m local structural setup, **not automatic A+ GEM certification**.
5. Invalidate bearish bias on `close > bearProtectedHigh`, bullish on `close < bullProtectedLow`.
6. Eight `alertcondition` events explicitly expose main LBOS, primary retracement, frozen mini BOS, BUY/SELL triggers in both directions.

**Risk / testing items:**
- `if newBearishMainBreak and showBearish` and `if newBullishMainBreak and showBullish` place **state creation behind visual toggles**. `showBearish`/`showBullish` are not display-only in this source. For evidence mapping, keep both enabled or audit a separate AMD code change; do **not** alter blindly in the FIX5 research patch.
- No explicit `barstate.isconfirmed` gating in the uploaded AMD source. Close-based rules are provisional intrabar until candle confirmation; use TradingView **Once Per Bar Close** for alerts and compare historical/realtime replay before relying on them.
- Although the source freezes mini BOS after retracement, it is independent from FIX5 `gemBridgeDir`, which is only a pivot-break directional proxy. AMD state cannot be inferred from that proxy.

## SNAP Trend Flips v5.3 — actual source behaviour

Distinct **1H origin / 5M proof** roles:

1. `f_snap1h()` finds confirmed 1H structural BOS + directional displacement + same-move FVG and qualifying OB origin; checks OB/FVG proximity, overlap **or** premium/discount (per input), and retains freshness/mitigation status. Its return values use `[1]` on the 1H series, consumed through `request.security(...,"60", f_snap1h(), lookahead=barmerge.lookahead_on)`; this is a deliberate prior-closed-HTF pattern, not evidence that 5m events are inherently confirmed.
2. Operational sweep/reclaim is **5M only** (`correctExecutionTF`); `bearishLiquiditySweep` / `bullishLiquiditySweep` require reference high/low swept (and optional reclaim), an active fresh 1H array and optional sweep-within-array interaction.
3. The source **freezes** MSS level, swept liquidity level, 1H OB/FVG array and sweep bar at arming. Same-direction sweeps do not continuously replace active candidates. Confirmed opposing sweeps can replace an unfinished sequence.
4. `bearishAPlus` / `bullishAPlus` require windowed post-sweep rejection, frozen 1H-array interaction, wick/body/50%-close qualification and optional engulfing/cooldown.
5. `bearishMSS` / `bullishMSS` require break of frozen MSS level, directional candle, strong MSS body/range and post-rejection timing. `bearishTrendFlip` / `bullishTrendFlip` combine MSS with still-valid rejection evidence.
6. Ten `alertcondition` families: new 1H buy/sell arrays; 5m BSL/SSL sweeps; bearish/bullish A+ rejection; bearish/bullish MSS; SNAP BUY/SELL Trend Flip.

**Risk / testing items:**
- The script restricts its Child sequence to 5m and does **not** output a native 1m proof event.
- The source has no explicit `barstate.isconfirmed` gate on the 5m signal booleans. Alert message text saying “confirmed” is not alone enough: require **Once Per Bar Close** and verify close-time actual events.
- “A+ rejection” is **Trend Flips-specific qualification**, not universal SNAP GEM A+ privilege; it does not itself establish DEX/EER Result or Parent promotion.
- A 1H array is an **authoritative location** but is not identical to a 1H structural Parent regime. Parent and POI authority must remain separate fields.

## Correct evidence layering for 15 GEM playbooks

**The 15 M-01–M-15 items are auction-pattern/model classifications, not a claim of 15 independent source-code indicators.** One auction episode may match multiple descriptive model labels, and multiple specialist indicator stages can contribute to one model, with timestamps and precedence.

| Layer | Source-owned event | Classification role | Not a substitute for |
|---|---|---|---|
| 1H Parent | SNAP NEXUS Parent regime; Trend Flips `fresh_1h_sell_array` / `fresh_1h_buy_array` | Regime and high-authority POI, recorded distinctly | A fresh 1H array alone is NOT a Parent reversal |
| 15M Bridge | AMD `bearish_main_lbos`, `primary_retracement`, `mini_bear_bos`, `amd_sell`; mirrors for buy | Bridge delivery, protected invalidation, 15m setup geometry and relevant local regime | 5m proof or new Parent authority |
| 15M liquidity/path | FIX5 native LSQ sweep, displacement, IFVG, A/B/D path, TIMEbase/LTS/CISD external streams when independently observed | Sequence evidence and ticket lifecycle | External indicator state simply because candles look similar |
| 5M Child | Trend Flips `bsl_sweep_reclaim` → `bearish_a_plus_rejection` → `bearish_mss` → `sell_trend_flip` (buy mirror); Pressure Map participation events | Proved local control transfer within frozen 1H array | 1m execution or NEXUS privilege |
| 1M proof | SNIPPET session-specific permission and/or independently verified 1m suite scripts | Child execution precision and entry permission | Automatic Parent promotion |
| NEXUS GEM | Proven timestamped source states + Story/EER evidence | `model_ids[]`, `PARENT_A_PLUS / TRANSITIONAL_CHILD_A_PLUS / UNCONFIRMED`, `FULL / REDUCED_TACTICAL / NONE` | Retroactive A+ assignment |

### Proposed cross-suite immutable event schema

```json
{
  "schema_version": "snap.gem.evidence.v0.1",
  "event_id": "source_id:source_sequence_id:bar_close_time:event_type",
  "source_id": "amd_trend_bias | snap_trend_flips | fix5 | ...",
  "source_version": "exact source version",
  "tickerid": "OANDA:XAUUSD",
  "timeframe": "15",
  "bar_open_time_ms": 0,
  "bar_close_time_ms": 0,
  "observed_at_ms": 0,
  "event_type": "amd_bearish_main_lbos",
  "side": "sell",
  "stage": "BRIDGE",
  "confirmed_at_bar_close": true,
  "source_sequence_id": "when source exposes one, otherwise derived durable event ID",
  "evidence": {"pivot_or_origin_price": null, "protected_level": null},
  "provenance": "source-native alert, NOT inferred from an unrelated script",
  "gem_certified": false
}
```

**No automatic trade should be placed from this contract alone.** Preserve source event-time versus receipt-time and a stale/unverified state. Other source messages need producer validation before consumption.

## Replay acceptance additions

1. AMD 15m: main LBOS → Fib touch → frozen Mini BOS → later Fib trigger, all distinct confirmed bars; assess protected level invalidation; verify `showBearish/showBullish` semantics.
2. Trend Flips 1H→5M: alert after **closed** 1H array; 5M sweep → valid rejection → MSS → trend-flip, with frozen array and same sequence; compare chart and alerts.
3. Counter-Parent test: 1H BEARISH Parent, 15m Bridge transitional, 5m buy-side Child: no false promotion of Parent; route independent tactical proof only after genuine Child sequence.
4. Identical timestamps cannot count as independent confirmation when two indicators derive from the same candle phenomenon; retain model overlaps without double-weighting score.
5. 15m FIX5 replay: native candidate/ticket class and broker-independent stop/TP outcomes unchanged; external event enrichment must not mutate frozen ticket state.
6. Source-lock AMD and Trend Flips exact versions before any connector adapter. Alert transport/rule engine is **not wired yet**.

## Integration decision

**Do not inject AMD and Trend Flips state machines into FIX5 in this patch.** Preserve their identities, use a timestamped external NEXUS evidence-aggregation contract, keep 1H Parent distinct from fresh 1H array locations, and retain separate 15M bridge and 5M Child phases. Audit stage first, wire explicit source-native event adapters next, test on trading replay (not just historical chart labels), and only then consider an optional execution gate. Human approval stays mandatory.
