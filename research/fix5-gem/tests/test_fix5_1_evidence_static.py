"""FIX5.1 source-only invariants; not a TradingView compiler or forward test."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
BASE = (ROOT / "SNAP_IFVG_LSQ_FIX5_GEM_RESEARCH.pine").read_text(encoding="utf-8")
CANDIDATE = (ROOT / "SNAP_IFVG_LSQ_FIX5_1_EVIDENCE_RESEARCH.pine").read_text(encoding="utf-8")


class EvidenceAuditContracts(unittest.TestCase):
    def test_six_ticket_births_and_entry_gates_unchanged(self):
        for source in (BASE, CANDIDATE):
            self.assertEqual(source.count("executionState := EXEC_ACTIVE"), 6)
            self.assertEqual(source.count("lastGemClassCode := f_gem_class_code("), 6)
            self.assertEqual(source.count("lastGemSnapshotTime := t15"), 6)
            self.assertEqual(source.count("and f_gem_entry_allowed("), 6)

    def test_entry_source_provenance(self):
        self.assertEqual(CANDIDATE.count('lastGemNativeEvidenceOrigin := "FIX5_A_NATIVE_ONLY"'), 2)
        self.assertEqual(CANDIDATE.count('lastGemNativeEvidenceOrigin := "FIX5_D_NATIVE_ONLY"'), 2)
        self.assertEqual(CANDIDATE.count('lastGemNativeEvidenceOrigin := "FIX5_B_REVERSAL_ONLY_PREDECESSOR_UNVERIFIED"'), 2)
        self.assertEqual(CANDIDATE.count("lastGemNativeLsqAtEntry := -1"), 2)
        self.assertEqual(CANDIDATE.count("lastGemNativeLsqAtEntry := bearModelLSQ"), 2)
        self.assertEqual(CANDIDATE.count("lastGemNativeLsqAtEntry := bullModelLSQ"), 2)

    def test_authoritative_ticket_logic_not_overridden(self):
        needles = [
            "if shortStopHit", "if longStopHit",
            "if shortTP1Now", "if longTP1Now",
            "shortTP2Now", "longTP2Now",
            "activeSequenceId := bearSequenceId",
            "activeSequenceId := bullSequenceId",
            "shortStopPrice := bearSweepExtreme",
            "longStopPrice := bullSweepExtreme",
            "gemRequireChildProof= input.bool(false,"
        ]
        for item in needles:
            self.assertIn(item, BASE)
            self.assertEqual(BASE.count(item), CANDIDATE.count(item), item)

    def test_no_external_gem_claims(self):
        self.assertIn('"gem_certified":false', CANDIDATE)
        self.assertNotIn('"gem_certified":true', CANDIDATE)
        self.assertIn('gem_playbook_mapping":"UNMAPPED', CANDIDATE)
        self.assertIn("gem_evidence_origin", CANDIDATE)
        self.assertIn("gem_native_lsq_at_entry", CANDIDATE)
        self.assertIn("FIX5_B_REVERSAL_ONLY_PREDECESSOR_UNVERIFIED", CANDIDATE)

    def test_path_c_does_not_rebirth_evidence(self):
        self.assertEqual(CANDIDATE.count("lastGemNativeEvidenceOrigin :="), 6)
        self.assertIn("pathCShortSignal := enablePathC", CANDIDATE)
        self.assertIn("pathCLongSignal := enablePathC", CANDIDATE)

    def test_data_window_trace(self):
        for label in (
            "FIX5.1 Entry Native LSQ (-1 unverified)",
            "FIX5.1 Entry Native IFVG Flag",
            "FIX5.1 Entry Native Path Touches",
            "FIX5.1 Entry Native Sweep Time",
            "FIX5.1 Entry Native Displacement Time",
        ):
            self.assertIn(label, CANDIDATE)


if __name__ == "__main__":
    unittest.main()
