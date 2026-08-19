MAX = 100
queue = []
visited = [0] * MAX
def bfs(graph, start, n):
    queue.append(start)
    visited[start] = 1
    while queue:
        v = queue.pop(0)
        print(v, end=" ")
        for i in range(n):
            if graph[v][i] == 1 and visited[i] == 0:
                queue.append(i)
                visited[i] = 1
n = int(input("Enter number of vertices: "))

graph = []
print("Enter adjacency matrix:")
for i in range(n):
    graph.append(list(map(int, input().split())))

start = int(input("Enter starting vertex: "))

print("BFS Traversal:", end=" ")
bfs(graph, start, n)