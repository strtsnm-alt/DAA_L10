edges = [[0, 1, 2], [1, 2, 3], [1, 3, 8], [1, 4, 5], [2, 4, 7], [0, 3, 6], [3, 4, 9]]
n = 5

edges.sort(key=lambda x: x[2])

component = [i for i in range(n)]
total_cost = 0

print("Kruskal's MST")
for edge in edges:
    u, v, wt = edge
    if component[u] != component[v]:
        print(f"{u} - {v} : {wt}")
        total_cost += wt
        
        old_comp = component[v]
        new_comp = component[u]
        for i in range(n):
            if component[i] == old_comp:
                component[i] = new_comp

print("Total Cost:", total_cost)
