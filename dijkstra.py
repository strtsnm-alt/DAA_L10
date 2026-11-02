inf = 100
graph = [[inf, 2, inf, 6, inf],
         [2, inf, 3, 8, 5],
         [inf, 3, inf, inf, 7],
         [6, 8, inf, inf, 9],
         [inf, 5, 7, 9, inf]]

n = len(graph)
dist = [inf] * n
visited = [False] * n

start = 0
dist[start] = 0

for _ in range(n):
    min_dist = inf
    u = -1
    for i in range(n):
        if not visited[i] and dist[i] < min_dist:
            min_dist = dist[i]
            u = i
            
    if u == -1:
        break
    visited[u] = True

    for v in range(n):
        if graph[u][v] != inf and not visited[v]:
            if dist[u] + graph[u][v] < dist[v]:
                dist[v] = dist[u] + graph[u][v]

print("Shortest distances from start:", dist)
