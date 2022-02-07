import Heap as hp

def bfs(graph,start):
    n = len(graph)
    visited = [False]*n
    parent = [None]*n
    visited[start] = True
    queue = [start]
    while queue:
        v = queue.pop(0)
        for u in graph[v]:
            if not visited[u]:
                parent[u] = v
                visited[u] = True
                queue.append(u)
    return parent

def Dijkstra(graph,start):
    n = len(graph)
    visited = [False]*n
    path = [None]*n
    cost = [float('inf')]*n
    cost[start] = 0
    # Priority Queue
    pq = hp.Heap(lambda a, b: a[0] < b[0])
    pq.push((0,start))
    while pq.Size() > 0:
        c , v = pq.pop()
        if not visited[v]:
            visited[v] = True
            for u, w in graph[v]:
                if not visited[u]:
                    if c + w < cost[u]:
                        cost[u] = c + w
                        path[u] = v
                        pq.push((cost[u],u))
    return path, cost
def BellmanFord(graph,start):
    n = len(graph)
    cost = [float('inf')]*n
    path = [None]*n
    cost[start] = 0

    for _ in range(n-1):
        for v in range(n):
            for u, w in graph[v]:
                if cost[v] + w < cost[u]:
                    cost[u] = cost[v] + w
                    path[u] = v
    
    for v in range(n):
        for u, w in graph[v]:
            if cost[v] + w < cost[u]:
                return None, None
    return path, cost