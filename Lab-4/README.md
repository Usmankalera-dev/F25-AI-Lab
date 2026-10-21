# Lab 4 - A* search and heuristic audit

In this lab I implemented A* search on the graph given in the lab manual and compared it with UCS. I also noted down the order in which nodes were expanded, and in the end I tried one run with a wrong (too large) heuristic value for C to see what happens.

## What you need

Python 3 only. No extra packages - the program uses `heapq` and `dataclasses`, which are part of Python itself.

## How to run

From the main folder of this repository:

```bash
python3 Lab-4/lab4_astar_audit.py
```

`output.txt` contains the result of my run, and the full report is in `Lab4_Report.docx`.

## Graph and heuristic

```text
S -> A (1), S -> B (4)
A -> C (2)
B -> G (5)
C -> G (3)

h(S)=5, h(A)=4, h(B)=4, h(C)=2, h(G)=0
start=S, goal=G
```

How the queue works: every entry is kept with (f, g, insertion number). If two entries have the same f and g, the one which was added first comes out first. One more thing - sometimes an old entry of a node is still sitting in the queue when a better path to that node has already been found. Such entries are skipped when they come out. In the expansion count I have not counted the goal node, but the processed trace shows every node taken out of the queue, including the goal.

## My results

| Run | Path | Cost | Processed trace | Expanded nodes (goal excluded) |
|---|---|---:|---|---:|
| A* with given heuristic | S → A → C → G | 6 | S → A → C → G | 3 |
| UCS (h(n)=0) | S → A → C → G | 6 | S → A → C → B → G | 4 |
| A* with h(C)=10 | S → B → G | 9 | S → A → B → G | 3 |

What I noticed: with the given heuristic, A* expanded 3 nodes and UCS expanded 4, and both gave the same best path with cost 6. The difference was only that UCS also expanded B, because without a heuristic it has no idea which side the goal is. When I changed h(C) to 10, A* took the S → B → G route with cost 9. The real remaining cost from C to G is only 3, so 10 was a clear overestimate, and that one wrong value made A* miss the better route. This is why the heuristic should never be greater than the actual remaining cost.
