import numpy as np
from .foam import total_foam

def gradient_psi(psi, agents, lambda_subj, eps=1e-6):
    """Численный градиент общей пены по состоянию Ψ."""
    # Для простоты: возмущаем M-матрицу.
    grad = np.zeros_like(psi['M'])
    base_phi = total_foam(psi, agents, lambda_subj)
    for i in range(psi['M'].shape[0]):
        for j in range(psi['M'].shape[1]):
            psi_pert = psi.copy()
            psi_pert['M'] = psi_pert['M'].copy()
            psi_pert['M'][i,j] += eps
            phi_pert = total_foam(psi_pert, agents, lambda_subj)
            grad[i,j] = (phi_pert - base_phi) / eps
    return grad

def update_psi(psi, agents, eta, lambda_subj):
    """Шаг градиентного спуска для Ψ."""
    grad = gradient_psi(psi, agents, lambda_subj)
    psi['M'] = psi['M'] - eta * grad
    return psi

def update_status(agents, psi, beta, lambda_subj, r_base=0.2, alpha_base=0.1):
    """Эволюция статуса S_i согласно dS/dt."""
    for i, agent in enumerate(agents):
        S_i = agent['S']
        # Базовый логистический рост
        growth = r_base * S_i * (1 - S_i)
        # Конкуренция с другими
        competition = sum(alpha_base * S_i * other['S'] for j, other in enumerate(agents) if j != i)
        # Вклад пены: аппроксимируем ∂Φ/∂S_i через влияние на общую пену
        phi_now = total_foam(psi, agents, lambda_subj)
        S_old = agent['S']
        agent['S'] += 0.01  # малое возмущение
        phi_pert = total_foam(psi, agents, lambda_subj)
        dphi_dS = (phi_pert - phi_now) / 0.01
        agent['S'] = S_old  # вернуть

        dS = growth - competition + beta * dphi_dS
        agent['S'] = max(0.0, min(1.0, agent['S'] + dS * 0.01))  # дискретный шаг
    return agents
