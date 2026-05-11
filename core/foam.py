import numpy as np

def cognitive_foam(psi):
    """Когнитивная пена = внутренние противоречия модели мира M."""
    # В реальной системе – анализ рассогласованности предиктов,
    # здесь для демонстрации: дисперсия матрицы уверенностей.
    return np.var(psi.get('M', np.eye(2)))

def self_foam(agent):
    """Внутренняя противоречивость self-слоя."""
    # Например, разница между явным и теневым self.
    return agent.get('self_conflict', 0.0)

def ego_foam(agent, others):
    """Эгоистическая пена: вред агента для других."""
    # Сумма отрицательных влияний на статус других.
    return sum(max(0, -agent.get('influence_on', {}).get(id(o), 0)) for o in others)

def social_foam(agent, others):
    """Социальная пена: нарушение кооперации."""
    # Измеряет, насколько действия агента разрушают общие связи.
    return sum(max(0, agent.get('betrayal', 0) - o.get('trust', 0)) for o in others)

def total_foam(psi, agents, lambda_subj=1.0):
    """Полная пена системы."""
    M = psi.get('M', np.eye(2))
    phi_cog = cognitive_foam(psi)
    phi_self = sum(self_foam(a) for a in agents)
    phi_ego = sum(ego_foam(a, agents) for a in agents)
    phi_soc = sum(social_foam(a, agents) for a in agents)
    return phi_cog + lambda_subj * (phi_self + phi_ego + phi_soc)
