def dijkstra(graph, source, n):
    INF = float('inf')
    distance = [INF] * n
    visited = [False] * n
    distance[source] = 0

    for count in range(n):
        u = -1
        min_distance = INF
        for i in range(n):
            if not visited[i] and distance[i] < min_distance:
                min_distance = distance[i]
                u = i
        if u == -1:
            break
        visited[u] = True
        for v in range(n):
            if (not visited[v] and
                graph[u][v] != 0 and
                distance[u] + graph[u][v] < distance[v]):
                distance[v] = distance[u] + graph[u][v]
    return distance
graph = [
    [0, 4, 1, 0, 0],
    [4, 0, 2, 5, 0],
    [1, 2, 0, 8, 10],
    [0, 5, 8, 0, 2],
    [0, 0, 10, 2, 0]
]
source = 0
n = len(graph)
distance = dijkstra(graph, source, n)
print("Shortest distances from vertex", source)
for i in range(n):
    print("Vertex", i, ":", distance[i])
