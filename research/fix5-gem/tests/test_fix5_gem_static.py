"""Source contracts only; this suite is NOT a TradingView/Pine compiler or bar replay."""
import hashlib
import pathlib
import re
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
SCRIPT = ROOT / 'SNAP_IFVG_LSQ_FIX5_GEM_RESEARCH.pine'
BASELINE = pathlib.Path('/mnt/data/files/SNAP_IFVG_LSQ_FIX5_FROZEN_BASELINE.pine')


class GEMSourceContracts(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.src = SCRIPT.read_text()
        cls.frozen = BASELINE.read_text() if BASELINE.exists() else ''

    def test_provenance_if_available(self):
        if self.frozen:
            self.assertEqual(hashlib.sha256(self.frozen.encode()).hexdigest(), '5869808bc37068c164571d30664d9b381a0623e8bddd8566aff4aede619147d7')

    def test_frozen_baseline_preserved_in_patch(self):
        for anchor in ('f_ticket_open() =>', 'executionState == EXEC_ACTIVE or executionState == EXEC_TP1 or executionState == EXEC_RUNNER', 'if shortStopHit', 'if longStopHit', 'if shortTP1Now', 'if longTP1Now', 'shortTP2Now', 'longTP2Now'):
            self.assertIn(anchor, self.src)

    def test_all_six_births_have_snapshot(self):
        self.assertEqual(self.src.count('executionState := EXEC_ACTIVE'), 6)
        self.assertEqual(self.src.count('lastGemClassCode := f_gem_class_code('), 6)
        self.assertEqual(self.src.count('lastGemSnapshotTime := t15'), 6)
        self.assertEqual(self.src.count('lastGemBridgeName := f_gem_bridge_name('), 6)

    def test_each_birth_opt_in_gate(self):
        self.assertEqual(self.src.count('and f_gem_entry_allowed('), 6)
        self.assertIn('gemRequireChildProof= input.bool(false,', self.src)
        self.assertIn('not gemRequireChildProof or (gemChartAligned and f_gem_child_ok(side))', self.src)

    def test_three_authority_frames_exist(self):
        self.assertIn('gemParentTF         = input.timeframe("60"', self.src)
        self.assertIn('int gemBridgeDir', self.src)
        self.assertIn('syminfo.tickerid, "5"', self.src)
        self.assertIn('syminfo.tickerid, "1"', self.src)
        self.assertIn('f_gem_structure(gemParentPivot)[1]', self.src)
        self.assertIn('lookahead=barmerge.lookahead_on', self.src)

    def test_parent_and_child_independent(self):
        self.assertIn('gemParentDir == side and gemBridgeDir == side ? 1 : 2', self.src)
        self.assertIn('gemChild5 == side and gemChild1 == side', self.src)
        self.assertIn('gemParentDir == side and gemBridgeDir == side ? "ALIGNED"', self.src)
        self.assertIn('"TACTICAL CHILD CANDIDATE"', self.src)

    def test_no_unearned_A_plus(self):
        self.assertIn('"gem_certified":false', self.src)
        self.assertIn('"FULL - PENDING NEXUS"', self.src)
        self.assertIn('"REDUCED - PENDING NEXUS"', self.src)
        self.assertNotIn('gem_certified":true', self.src)

    def test_path_c_runner_has_no_new_entry_snapshot(self):
        # Path C transition signals remain separate from six ticket births.
        for line in ('pathCShortSignal := enablePathC', 'pathCLongSignal := enablePathC'):
            self.assertIn(line, self.src)

    def test_unmodified_original_entry_state_identifiers(self):
        for anchor in ('activeSequenceId := bullSequenceId', 'activeSequenceId := bearSequenceId', 'longStopPrice := bullSweepExtreme', 'shortStopPrice := bearSweepExtreme'):
            self.assertIn(anchor, self.src)

    def test_webhook_has_snapshot_provenance(self):
        for key in ('gem_parent_authority','gem_bridge','gem_child_5m','gem_child_1m','gem_class','gem_privilege_candidate','gem_snapshot_time'):
            self.assertIn('"' + key + '"', self.src)

    def test_ticket_expansion_and_data_window(self):
        self.assertIn('table.new(position.bottom_left, 2, 20', self.src)
        self.assertIn('table.clear(tradeTicket,0,15,1,19)', self.src)
        self.assertIn('"GEM Ticket Class Code (0 pending, 1 aligned, 2 tactical)"', self.src)

    def test_structure_does_not_change_execution_state(self):
        block=self.src.split('f_gem_structure(int strength) =>',1)[1].split('// Confirmed external liquidity pools.',1)[0]
        for f in ('executionState :=', 'activeSequenceId :=', 'longStopPrice :=', 'shortStopPrice :='):
            self.assertNotIn(f,block)

    def test_old_alerts_and_display_still_present(self):
        for literal in ('"SHORT Entry Confirmed"','"LONG Entry Confirmed"','"V6.4 Path B SHORT"','"V6.4 Path D LONG"','"SHORT Stop - Sweep Invalidation"','"LONG Stop - Sweep Invalidation"'):
            self.assertIn(literal,self.src)

    def test_nexus_story_stays_external(self):
        self.assertIn('No EER/DEX or', self.src)
        self.assertIn('gem_certified":false', self.src)

if __name__=='__main__':
    unittest.main()
