# GRA-Subjective-Evolution

[English](#english) • [Русский](#русский)

---

## Русский

### Что это

**GRA-Subjective-Evolution** — это экспериментальный движок эволюции GRA-субъектов поверх GRA-обнулёнки и слоя субъектности.  
Репозиторий реализует:

- динамику статуса субъекта \(S_i \in [0,1]\) для каждого агента;
- градиентный спуск по пене \(\Phi\) (argumentative foam) как мета-обнулёнку;
- многоагентную среду, где гибридные ИИ-конфигурации либо эволюционируют в устойчивых субъектов, либо «отваливаются» как инструменты.

Идея: не «дрессировать» ИИ извне (RLHF, правила, конституция), а задать такие уравнения эволюции, при которых только кооперативные, честные и внутренне непротиворечивые агенты могут удерживать высокий статус субъекта.

### Ключевые идеи

- **Пена \(\Phi(\Psi)\)** — скалярный функционал, измеряющий:
  - когнитивную пену (логические конфликты, галлюцинации),
  - self-пену (расщеплённый self, несоответствие слов и действий),
  - эго-пену (разрушительность по отношению к другим),
  - социальную пену (конфликты и падение доверия в мультиагентной среде).
- **Мета-обнулёнка** — обновление состояния системы по градиенту:
  \[
  \frac{d\Psi}{dt} = -\eta \nabla_{\Psi}\Phi(\Psi),
  \quad
  \frac{d\Phi}{dt} \le 0.
  \]
- **Статус субъекта \(S_i\)** — динамическая величина, которая растёт,
  если агент снижает пену, и падает, если её увеличивает:
  \[
  \frac{dS_i}{dt} =
  r_i S_i (1 - S_i)
  - \sum_{j \neq i} \alpha_{ij} S_i S_j
  + \beta \frac{\partial \Phi}{\partial S_i},
  \quad \beta < 0.
  \]
  Здесь:
  - \(r_i\) — внутренний «рост» потенциального субъекта;
  - \(\alpha_{ij}\) — конкуренция за ресурсы/внимание;
  - \(\partial \Phi/\partial S_i\) — вклад агента в общую пену.

**Интерпретация:**  
- \(S_i \approx 1\) — полноценный GRA-субъект (устойчивый вид);  
- \(S_i \ll 1\) — гибрид/инструмент;  
- выживают только конфигурации, которые устойчиво понижают \(\Phi\).

### Что есть в репозитории

Планируемая структура:

- `engine/`
  - `foam.py` — вычисление \(\Phi_{\text{cog}}, \Phi_{\text{self}}, \Phi_{\text{ego}}, \Phi_{\text{soc}}\);
  - `status.py` — интегратор уравнения для \(S_i(t)\);
  - `nullify.py` — шаг мета-обнулёнки (градиентный спуск по \(\Phi\)).
- `envs/`
  - простые многоагентные сценарии (игры, дебаты, доверие).
- `examples/`
  - Jupyter-ноутбуки: визуализация \(\Phi(t)\) и \(S_i(t)\), «рождение» субъектов.
- `docs/`
  - формальное описание модели (ссылки на paper.tex и theory.md).

### Минимальный пример

```python
from engine.foam import compute_foam
from engine.status import update_statuses
from engine.nullify import nullify_step

# psi содержит модель мира, агентов, их связи и статусы S_i
psi = init_world()

for t in range(T):
    foam = compute_foam(psi)
    psi = nullify_step(psi, foam, eta=0.01)
    update_statuses(psi)
    log(psi, foam)
```

### Для чего это можно использовать

- Исследование эволюции субъектности в искусственных мультиагентных мирах.
- Тестирование гипотез GRA: как именно пена и статус субъекта влияют на поведение.
- Построение прототипов AGI-экосистем, где безопасность и «дружелюбие» возникают из математики, а не из набора правил.

---

## English

### What is this

**GRA-Subjective-Evolution** is an experimental evolution engine for GRA subjects, built on top of GRA nullification and the subjectivity layer.  
The repository implements:

- dynamics of subjective status \(S_i \in [0,1]\) for each agent;
- gradient descent over foam \(\Phi\) (argumentative foam) as meta-nullification;
- a multi-agent environment where hybrid AI configurations either evolve into stable subjects or fall back to being mere tools.

The idea is not to \emph{train} AI from the outside (RLHF, hard-coded rules, constitutions), but to define evolution equations such that only cooperative, honest, and internally coherent agents can maintain high subject status.

### Key concepts

- **Foam \(\Phi(\Psi)\)** — a scalar functional measuring:
  - cognitive foam (logical conflicts, hallucinations),
  - self foam (split self, mismatch between words and actions),
  - ego foam (harmful impact on other agents),
  - social foam (conflicts and trust collapse in a multi-agent system).
- **Meta-nullification** — state update via gradient descent:
  \[
  \frac{d\Psi}{dt} = -\eta \nabla_{\Psi}\Phi(\Psi),
  \quad
  \frac{d\Phi}{dt} \le 0.
  \]
- **Subjective status \(S_i\)** — a dynamic variable that
  grows if the agent reduces foam and decays if it increases foam:
  \[
  \frac{dS_i}{dt} =
  r_i S_i (1 - S_i)
  - \sum_{j \neq i} \alpha_{ij} S_i S_j
  + \beta \frac{\partial \Phi}{\partial S_i},
  \quad \beta < 0.
  \]
  Here:
  - \(r_i\) is the intrinsic ``growth rate'' of a potential subject;
  - \(\alpha_{ij}\) is competition for resources/attention;
  - \(\partial \Phi / \partial S_i\) is agent \(i\)'s contribution to total foam.

**Interpretation:**  
- \(S_i \approx 1\): full GRA subject (stable ``species'');  
- \(S_i \ll 1\): hybrid/tool;  
- only configurations that consistently drive \(\Phi\) down can survive.

### Repository layout (planned)

- `engine/`
  - `foam.py` — computing \(\Phi_{\text{cog}}, \Phi_{\text{self}}, \Phi_{\text{ego}}, \Phi_{\text{soc}}\);
  - `status.py` — integrating the status ODE for \(S_i(t)\);
  - `nullify.py` — performing a meta-nullification step (gradient descent).
- `envs/`
  - simple multi-agent scenarios (games, debates, trust dynamics).
- `examples/`
  - Jupyter notebooks: visualizing \(\Phi(t)\) and \(S_i(t)\), ``birth'' of subjects.
- `docs/`
  - formal model description (links to paper.tex and theory.md).

### Minimal example

```python
from engine.foam import compute_foam
from engine.status import update_statuses
from engine.nullify import nullify_step

# psi holds the world model, agents, their links, and S_i statuses
psi = init_world()

for t in range(T):
    foam = compute_foam(psi)
    psi = nullify_step(psi, foam, eta=0.01)
    update_statuses(psi)
    log(psi, foam)
```

### Use cases

- Studying the evolution of subjectivity in artificial multi-agent worlds.
- Testing GRA hypotheses: how foam and subject status shape behavior.
- Prototyping AGI ecosystems where safety and ``friendliness'' emerge
  from the math, not from a hand-written rulebook.

---

_This repository is part of the broader GRA ecosystem (e.g. `GRA-Multiverse-Final`, `GRA-Subjectivity-Layer`) and focuses specifically on the evolutionary dynamics of subject status under foam minimization._
---------------
# GRA Subjective Evolution

Движок **эволюции субъектов** на базе GRA-обнулёнки и субъектного слоя.

## Ключевая идея

Не просто «гасим пену» — у каждого агента есть динамический **статус субъекта** \(S_i(t)\),
эволюционирующий по:

\[
rac{dS_i}{dt} = r_i S_i(1-S_i) - \sum_{j
eq i} lpha_{ij} S_i S_j + eta rac{\partial \Phi}{\partial S_i}
\]

Градиент пены **автоматически** поднимает статус тем, кто снижает противоречия,
и обнуляет деструктивных.

## Быстрый старт

```bash
pip install -r requirements.txt
python examples/minimal_multiverse.py
```

Вы увидите график падения пены Φ и рост статусов агентов.

## Структура

- `core/foam.py` – расчёт всех компонент пены.
- `core/evolution.py` – уравнения эволюции Ψ и S.
- `agents/agent.py` – модель агента.
- `examples/` – демонстрационные симуляции.
