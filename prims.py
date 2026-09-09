def prim_mst(graph):
    V = len(graph)
    parent = [-1] * V
    key = [float('inf')] * V
    mst_set = [False] * V
    key[0] = 0
    for _ in range(V):
        min_key = float('inf')
        u = -1
        for v in range(V):
            if not mst_set[v] and key[v] < min_key:
                min_key = key[v]
                u = v
        if u == -1:
            break
        mst_set[u] = True
        for v in range(V):
            weight = graph[u][v]
            if weight > 0 and not mst_set[v] and weight < key[v]:
                key[v] = weight
                parent[v] = u
    print("Edge \tWeight")
    for i in range(1, V):
        if parent[i] != -1:
            print(f"{parent[i]} - {i} \t{graph[i][parent[i]]}")
graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]

prim_mst(graph)