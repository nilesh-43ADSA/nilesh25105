def floyd_warshall(graph, n):
    INF = float('inf')
    dist = [row[:] for row in graph]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if (dist[i][k] != INF and
                    dist[k][j] != INF and
                    dist[i][k] + dist[k][j] < dist[i][j]):
                    dist[i][j] = dist[i][k] + dist[k][j]
    print("Shortest Distance Matrix:")
    for i in range(n):
        for j in range(n):
            if dist[i][j] == INF:
                print("INF", end="\t")
            else:
                print(dist[i][j], end="\t")
        print()
INF = float('inf')
graph = [
    [0,   11,  INF, 10],
    [INF, 0,   2,  INF],
    [INF, INF, 0,   1],
    [INF, INF, INF, 0]
]
n = len(graph)
floyd_warshall(graph, n)
