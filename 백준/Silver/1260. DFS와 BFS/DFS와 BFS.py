import sys
from collections import deque

N, M, V = map(int, sys.stdin.readline().split())
graph = {i: [] for i in range(1, N + 1)} 

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)  
    graph[v].append(u)  
  
dfsVisited = set()

# DFS
def dfs(node): 
  if node not in dfsVisited:
    print(node, end=' ')
    dfsVisited.add(node)
    for neighbor in sorted(graph[node]):
        dfs(neighbor)

# BFS
def bfs(graph, start):
    visited = [False] * (max(graph) + 1)  
    queue = deque([start])
    visited[start] = True  
    to_print = []  
    while queue:
        v = queue.popleft()
        to_print.append(v) 
        for i in sorted(graph[v]): 
            if not visited[i]:
                queue.append(i)
                visited[i] = True 
    print(*to_print)  

dfs(V)
print()
bfs(graph, V)