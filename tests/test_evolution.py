import unittest
import numpy as np
from core.evolution import update_psi, update_status
from core.foam import total_foam

class TestEvolution(unittest.TestCase):
    def test_foam_decreases(self):
        agents = [{'S':0.5, 'self_conflict':0.1, 'influence_on':{}, 'betrayal':0, 'trust':1}]
        psi = {'M': np.eye(2)}
        eta, beta, lam = 0.1, -0.2, 1.0
        phi_before = total_foam(psi, agents, lam)
        psi = update_psi(psi, agents, eta, lam)
        phi_after = total_foam(psi, agents, lam)
        self.assertLessEqual(phi_after, phi_before + 1e-9)

    def test_status_boundaries(self):
        agents = [{'S':0.0, 'self_conflict':0.0, 'influence_on':{}, 'betrayal':0, 'trust':1}]
        psi = {'M': np.eye(2)}
        agents_updated = update_status(agents, psi, beta=-0.2, lambda_subj=1.0)
        for a in agents_updated:
            self.assertTrue(0.0 <= a['S'] <= 1.0)

if __name__ == '__main__':
    unittest.main()
