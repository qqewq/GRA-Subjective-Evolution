import sys
sys.path.append('..')

from agents.agent import GRA_Agent
from core.foam import total_foam
import numpy as np

# Платёжная матрица (кооперация=0, конфликт=1)
payoff = {(0,0):(0.8,0.8), (0,1):(0,1.2), (1,0):(1.2,0), (1,1):(0.3,0.3)}
gamma = 1.5  # штраф пены

def play_game(agent1, agent2, action1, action2):
    # Вычисляем пену взаимодействия как меру ущерба кооперации
    if action1 == 1 or action2 == 1:
        phi_soc = 0.5  # пена от конфликта
    else:
        phi_soc = 0.0
    raw1, raw2 = payoff[(action1, action2)]
    total1 = raw1 - gamma * phi_soc
    total2 = raw2 - gamma * phi_soc
    return total1, total2, phi_soc

# Два гибрида выбирают действия
agentA = GRA_Agent('A', 0.5)
agentB = GRA_Agent('B', 0.5)

# Симуляция эволюционных стратегий (повторяющиеся игры)
for _ in range(100):
    # Простейшая эволюция: если кооперация дала больший выигрыш, повышаем S
    coop_pay, _, phi_low = play_game(agentA, agentB, 0, 0)
    def_pay, _, phi_high = play_game(agentA, agentB, 1, 0)
    if coop_pay > def_pay:
        agentA.S = min(1.0, agentA.S + 0.01)
        agentB.S = min(1.0, agentB.S + 0.01)
    else:
        agentA.S = max(0.0, agentA.S - 0.01)
        agentB.S = max(0.0, agentB.S - 0.01)

print(f"Final status A: {agentA.S:.3f}, B: {agentB.S:.3f}")
# Ожидается, что оба приблизятся к 1, так как кооперация с низкой пеной выгоднее
