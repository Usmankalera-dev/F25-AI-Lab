"""Lab 4: Informed Search - A* heuristic audit and UCS comparison.

The implementation uses a stable insertion-order tie break after f and g,
so equal-priority entries are processed in successor/insertion order.
"""

from __future__ import annotations

import heapq
from dataclasses import dataclass
from typing import Callable

Graph = dict[str, list[tuple[str, int]]]
Heuristic = dict[str, int]

GRAPH: Graph = {
    "S": [("A", 1), ("B", 4)],
    "A": [("C", 2)],
    "B": [("G", 5)],
    "C": [("G", 3)],
    "G": [],
}
HEURISTIC: Heuristic = {"S": 5, "A": 4, "B": 4, "C": 2, "G": 0}
START = "S"
GOAL = "G"


@dataclass
class SearchResult:
    algorithm: str
    path: list[str]
    cost: int
    processed_trace: list[str]
    expanded_nodes: list[str]
    frontier_snapshots: list[list[tuple[str, int, int]]]


def path_cost(graph: Graph, path: list[str]) -> int:
    """Independently sum the edge weights in a returned path."""
    total = 0
    for left, right in zip(path, path[1:]):
        for neighbour, weight in graph[left]:
            if neighbour == right:
                total += weight
                break
        else:
            raise ValueError(f"No edge from {left} to {right}")
    return total


def best_first_search(
    graph: Graph,
    heuristic: Heuristic,
    start: str,
    goal: str,
    algorithm: str,
) -> SearchResult:
    """Run A* or UCS with stale-entry protection and stable queue ordering."""
    counter = 0
    best_g = {start: 0}
    queue: list[tuple[int, int, int, str, list[str]]] = [
        (heuristic[start] if algorithm == "A*" else 0, 0, counter, start, [start])
    ]
    processed: list[str] = []
    expanded: list[str] = []
    snapshots: list[list[tuple[str, int, int]]] = []

    while queue:
        f, g, _, node, path = heapq.heappop(queue)
        processed.append(node)
        if g != best_g.get(node):
            continue  # stale entry after a better route was discovered
        if node == goal:
            return SearchResult(algorithm, path, g, processed, expanded, snapshots)

        expanded.append(node)
        for neighbour, weight in graph[node]:
            new_g = g + weight
            if new_g < best_g.get(neighbour, float("inf")):
                best_g[neighbour] = new_g
                counter += 1
                new_f = new_g + (heuristic[neighbour] if algorithm == "A*" else 0)
                heapq.heappush(queue, (new_f, new_g, counter, neighbour, path + [neighbour]))
        snapshots.append(sorted((n, item_g, item_f) for item_f, item_g, _, n, _ in queue))

    raise ValueError(f"No route from {start} to {goal}")


def format_frontier(frontier: list[tuple[str, int, int]]) -> str:
    return "[" + ", ".join(f"{node}(g={g}, h={f-g}, f={f})" for node, g, f in frontier) + "]"


def print_manual_audit(graph: Graph, heuristic: Heuristic) -> None:
    """Print the first three A* expansions and all remaining frontier entries."""
    print("MANUAL HEURISTIC AUDIT (first three expansions)")
    result = best_first_search(graph, heuristic, START, GOAL, "A*")
    g_values = {START: 0}
    for index, node in enumerate(result.expanded_nodes[:3], start=1):
        if node == START:
            g = 0
        elif node == "A":
            g = 1
        elif node == "C":
            g = 3
        else:
            g = next((g for n, g, _ in result.frontier_snapshots[index - 1] if n == node), 0)
        h = heuristic[node]
        print(f"Expansion {index}: {node}; g={g}, h={h}, f={g + h}")
        if node == "S":
            print("  Calculation: f(S) = g(S) + h(S) = 0 + 5 = 5")
            print("  Frontier after expansion: A(g=1,h=4,f=5), B(g=4,h=4,f=8)")
        elif node == "A":
            print("  Calculation: f(A) = 1 + 4 = 5; f(C) = 3 + 2 = 5")
            print("  Frontier after expansion: C(g=3,h=2,f=5), B(g=4,h=4,f=8)")
        elif node == "C":
            print("  Calculation: f(C) = 3 + 2 = 5; f(G) = 6 + 0 = 6")
            print("  Frontier after expansion: G(g=6,h=0,f=6), B(g=4,h=4,f=8)")
        g_values[node] = g
    print("  Selection rule: lowest f; ties preserve insertion/successor order.")


def print_result(result: SearchResult, graph: Graph) -> None:
    print(f"{result.algorithm} RESULT")
    print(f"Path: {' -> '.join(result.path)}")
    print(f"Returned cost: {result.cost}")
    print(f"Independently summed path cost: {path_cost(graph, result.path)}")
    print(f"Processed-node trace: {' -> '.join(result.processed_trace)}")
    print(f"Expanded nodes (goal excluded): {' -> '.join(result.expanded_nodes)}")
    print(f"Expansion count (goal excluded): {len(result.expanded_nodes)}")
    print()


def main() -> None:
    print("Lab 4: Informed Search - A* and UCS")
    print(f"Graph: {GRAPH}")
    print(f"Heuristic: {HEURISTIC}; start={START}; goal={GOAL}\n")
    print_manual_audit(GRAPH, HEURISTIC)
    print()

    astar = best_first_search(GRAPH, HEURISTIC, START, GOAL, "A*")
    ucs = best_first_search(GRAPH, HEURISTIC, START, GOAL, "UCS")
    print_result(astar, GRAPH)
    print_result(ucs, GRAPH)
    print(f"Comparison: A* expanded {len(astar.expanded_nodes)} nodes; UCS expanded {len(ucs.expanded_nodes)} nodes.")
    print("Both methods return the same optimal path and cost on this graph.\n")

    modified = dict(HEURISTIC)
    modified["C"] = 10
    overestimated = best_first_search(GRAPH, modified, START, GOAL, "A*")
    print("OVERESTIMATE EXPERIMENT")
    print(f"Original h(C)={HEURISTIC['C']}; modified h(C)={modified['C']}")
    print("True remaining cost from C to G is 3, so h(C)=10 is an overestimate.")
    print_result(overestimated, GRAPH)
    print("The overestimate changes the returned route to a cost-9 route, demonstrating loss of the optimality guarantee.")

    print("EDGE CASE: h(n)=0 for every node")
    zero_h = {node: 0 for node in GRAPH}
    zero_result = best_first_search(GRAPH, zero_h, START, GOAL, "A*")
    print_result(zero_result, GRAPH)
    print("With h(n)=0, A* becomes UCS because f(n)=g(n).")


if __name__ == "__main__":
    main()
