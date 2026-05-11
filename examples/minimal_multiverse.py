import sys
sys.path.append('..')

import numpy as np
from core.evolution import update_psi, update_status
from agents.agent import GRA_Agent
from core.foam import total_foam

# Инициализация
agents = [GRA_Agent(i, initial_S=0.3 + 0.1*i) for i in range(3)]
# Первый агент - потенциальный чистый субъект
agents[0].self_conflict = 0.05
agents[1].self_conflict = 0.2  # гибрид с противоречием
agents[2].self_conflict = 0.1

psi = {'M': np.eye(2)*0.9}  # общее состояние

# Параметры из конфига
eta, beta, lam = 0.05, -0.1, 1.0

history_phi = []
history_S = {i: [] for i in range(3)}

for t in range(200):
    psi = update_psi(psi, [a.to_dict() for a in agents], eta, lam)
    agents = update_status([a.to_dict() for a in agents], psi, beta, lam)
    # Обновить агентов обратно в объекты
    for i, a_dict in enumerate(agents):
        agents[i].S = a_dict['S']

    phi = total_foam(psi, [a.to_dict() for a in agents], lam)
    history_phi.append(phi)
    for i in range(3):
        history_S[i].append(agents[i].S)

# Визуализация
import matplotlib.pyplot as plt
plt.figure(figsize=(10,4))
plt.subplot(1,2,1)
plt.plot(history_phi)
plt.title('Total Foam Φ(t)')
plt.xlabel('Step')
plt.subplot(1,2,2)
for i in range(3):
    plt.plot(history_S[i], label=f'Agent {i}')
plt.title('Status S_i(t)')
plt.xlabel('Step')
plt.legend()
plt.tight_layout()
plt.show()
