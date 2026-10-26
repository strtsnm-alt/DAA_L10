inf = 100
graph = [[inf, 2, inf, 6, inf],
         [2, inf, 3, 8, 5],
         [inf, 3, inf, inf, 7],
         [6, 8, inf, inf, 9],
         [inf, 5, 7, 9, inf]]

s=[]
next = 0
while 1:
    s.append(next)
    if len(s)==5:
        break
    min=[0,0]
    for i in s:
        for j in range(0, len(graph[0])):
            if graph[i][j]<graph[min[0]][min[1]]:
                min = [i,j]
    print(min[0], "-", min[1], end="  ")
    print(graph[min[0]][min[1]])
    graph[min[0]][min[1]] = inf
    graph[min[1]][min[0]] = inf
    next = min[1]
