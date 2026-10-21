import heapq

graph = {
    "S": [("A", 1), ("B", 4)],
    "A": [("C", 2)],
    "B": [("G", 5)],
    "C": [("G", 3)],
    "G": [],
}
heuristic = {"S": 5, "A": 4, "B": 4, "C": 2, "G": 0}
start = "S"
goal = "G"


def path_cost(path):
    total = 0
    for i in range(len(path) - 1):
        for nb, w in graph[path[i]]:
            if nb == path[i + 1]:
                total = total + w
    return total


def search(use_h, h):
    counter = 0
    best_g = {start: 0}
    first_f = h[start] if use_h else 0
    queue = [(first_f, 0, counter, start, [start])]
    processed = []
    expanded = []
    while queue:
        f, g, _, node, path = heapq.heappop(queue)
        processed.append(node)
        if g != best_g.get(node):
            continue
        if node == goal:
            return path, g, processed, expanded, best_g
        expanded.append(node)
        for nb, w in graph[node]:
            new_g = g + w
            if new_g < best_g.get(nb, float("inf")):
                best_g[nb] = new_g
                counter = counter + 1
                new_f = new_g + (h[nb] if use_h else 0)
                heapq.heappush(queue, (new_f, new_g, counter, nb, path + [nb]))


def print_audit():
    print("MANUAL HEURISTIC AUDIT (first three expansions)")
    path, cost, processed, expanded, best_g = search(True, heuristic)
    for i, node in enumerate(expanded[:3], start=1):
        g = best_g[node]
        h = heuristic[node]
        print(f"Expansion {i}: {node}; g={g}, h={h}, f={g + h}")
        if node == "S":
            print("  Calculation: f(S) = g(S) + h(S) = 0 + 5 = 5")
            print("  Frontier after expansion: A(g=1,h=4,f=5), B(g=4,h=4,f=8)")
        elif node == "A":
            print("  Calculation: f(A) = 1 + 4 = 5; f(C) = 3 + 2 = 5")
            print("  Frontier after expansion: C(g=3,h=2,f=5), B(g=4,h=4,f=8)")
        elif node == "C":
            print("  Calculation: f(C) = 3 + 2 = 5; f(G) = 6 + 0 = 6")
            print("  Frontier after expansion: G(g=6,h=0,f=6), B(g=4,h=4,f=8)")
    print("  Selection rule: lowest f; ties preserve insertion/successor order.")


def print_result(name, result):
    path, cost, processed, expanded, best_g = result
    print(name + " RESULT")
    print("Path: " + " -> ".join(path))
    print(f"Returned cost: {cost}")
    print(f"Independently summed path cost: {path_cost(path)}")
    print("Processed-node trace: " + " -> ".join(processed))
    print("Expanded nodes (goal excluded): " + " -> ".join(expanded))
    print(f"Expansion count (goal excluded): {len(expanded)}")
    print()


def main():
    print("Lab 4: Informed Search - A* and UCS")
    print(f"Graph: {graph}")
    print(f"Heuristic: {heuristic}; start={start}; goal={goal}\n")
    print_audit()
    print()

    astar = search(True, heuristic)
    ucs = search(False, heuristic)
    print_result("A*", astar)
    print_result("UCS", ucs)
    print(f"Comparison: A* expanded {len(astar[3])} nodes; UCS expanded {len(ucs[3])} nodes.")
    print("Both methods return the same optimal path and cost on this graph.\n")

    modified = dict(heuristic)
    modified["C"] = 10
    over = search(True, modified)
    print("OVERESTIMATE EXPERIMENT")
    print(f"Original h(C)={heuristic['C']}; modified h(C)={modified['C']}")
    print("True remaining cost from C to G is 3, so h(C)=10 is an overestimate.")
    print_result("A*", over)
    print("The overestimate changes the returned route to a cost-9 route, demonstrating loss of the optimality guarantee.")

    print("EDGE CASE: h(n)=0 for every node")
    zero_h = {node: 0 for node in graph}
    zero = search(True, zero_h)
    print_result("A*", zero)
    print("With h(n)=0, A* becomes UCS because f(n)=g(n).")


main()
