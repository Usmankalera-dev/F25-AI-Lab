g = {"S": [("A", 1), ("B", 4)], "A": [("C", 2)], "B": [("G", 5)], "C": [("G", 3)], "G": []}
h = {"S": 5, "A": 4, "B": 4, "C": 2, "G": 0}
true = {"S": 6, "A": 5, "B": 5, "C": 3, "G": 0}

def astar(s, t, h):
    f = [(h[s], 0, s, [s])]
    best = {s: 0}
    done = []
    vals = []
    while f:
        f.sort()
        fv, cost, n, p = f.pop(0)
        if cost != best[n]:
            continue
        done.append(n)
        vals.append((n, cost, h[n], fv))
        if n == t:
            return cost, p, done, vals
        for x, d in g[n]:
            nc = cost + d
            if nc < best.get(x, 999):
                best[x] = nc
                f.append((nc + h[x], nc, x, p + [x]))

print("Task 1 A* g, h, f:", astar("S", "G", h)[3])
print("Task 2 A*:", astar("S", "G", h))
print("Task 2 UCS:", astar("S", "G", {k: 0 for k in h}))
print("Task 2 expansions, A* 3, UCS 4, goal not counted")
print("Audit h <= true:", [(k, h[k] <= true[k]) for k in h])
h2 = dict(h)
h2["C"] = 10
print("Task 3 overestimate h(C) 2 to 10:", astar("S", "G", h2))
