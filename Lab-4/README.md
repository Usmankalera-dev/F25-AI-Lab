# Lab 4: Informed Search — Heuristics & A*

This lab implements A* on the supplied weighted campus graph, compares it with Uniform-Cost Search (UCS), records expansion traces, and tests an overestimated heuristic.

## Requirements

- Python 3.9+
- No third-party packages

## Run

From the repository root:

```bash
python3 Lab-4/lab4_astar_audit.py
```

The captured run is available in [`output.txt`](output.txt). The full explanation and analysis are in [`Lab4_Report.docx`](Lab4_Report.docx).

## Problem data

```text
S -> A (1), S -> B (4)
A -> C (2)
B -> G (5)
C -> G (3)

h(S)=5, h(A)=4, h(B)=4, h(C)=2, h(G)=0
start=S, goal=G
```

The queue uses `(f, g, insertion_order)` as its priority. Equal-priority entries preserve successor/insertion order. Stale queue entries are ignored after a better `g` value is found. Expansion counts exclude the goal node, while the processed trace includes the goal and shows every popped entry.

## Results

| Run | Path | Cost | Processed trace | Expanded nodes (goal excluded) |
|---|---|---:|---|---:|
| A* with supplied heuristic | S → A → C → G | 6 | S → A → C → G | 3 |
| UCS (`h(n)=0`) | S → A → C → G | 6 | S → A → C → B → G | 4 |
| A* with `h(C)=10` | S → B → G | 9 | S → A → B → G | 3 |

The supplied heuristic makes A* expand one fewer non-goal node than UCS while preserving the optimal route. Changing only `h(C)` from 2 to 10 overestimates C's true remaining cost of 3 and causes A* to return the cost-9 route, so admissibility is necessary for the optimality guarantee.
