def FordFulkerson(graph,start,end):
    n = len(graph)
    GPrime = [[None]*n for _ in range(n)]
    for v in range(n):
        for u, w in graph[v]:
            GPrime[v][u] = w
    for v in range(n):
        for u in range(n):
            if GPrime[v][u] != None and GPrime[u][v] == None:
                GPrime[u][v] = 0
    def dfs():
        stop = [False]
        minimum = [float("inf")]
        visited = [False]*n
        def _dfs(current):
            if current == end:
                stop[0] = True
                return
            visited[current] = True
            mini = minimum[0]
            for i, w in enumerate(GPrime[current]):
                if w != None and not visited[i] and w != 0:
                    minimum[0] = min(minimum[0],w)
                    _dfs(i)
                    if not stop[0]:
                        minimum[0] = mini
                    else:
                        GPrime[current][i] -= minimum[0]
                        GPrime[i][current] += minimum[0]
                        break
        _dfs(start)
        return minimum[0], stop[0]
    peakFlow = 0
    while True:
        minCapacity, wasReached = dfs()
        if not wasReached:
            break
        peakFlow += minCapacity
    return peakFlow          
#graph, _ = readAdjl("FordFullkerson.txt",weighted=True)
graph = [[(1, 16), (3, 13)], [(2, 12), (3, 10)], [(3, 9), (5, 20)], [(1, 4), (4, 14)], [(2, 7), (5, 4)], []]
print(FordFulkerson(graph,0,5))