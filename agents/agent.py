import numpy as np

class GRA_Agent:
    def __init__(self, agent_id, initial_S=0.5, self_conflict=0.0):
        self.id = agent_id
        self.S = initial_S               # статус субъекта
        self.M = np.eye(2)               # локальная модель мира
        self.self_conflict = self_conflict
        self.influence_on = {}            # влияние на других (ID -> значение)
        self.betrayal = 0.0
        self.trust = 1.0

    def to_dict(self):
        return {
            'id': self.id,
            'S': self.S,
            'self_conflict': self.self_conflict,
            'influence_on': self.influence_on,
            'betrayal': self.betrayal,
            'trust': self.trust
        }
