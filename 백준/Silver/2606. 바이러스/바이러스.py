import sys 
from collections import deque

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
graph = {i: [] for i in range(1, N + 1)} 
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)  
    graph[v].append(u)

visited = set()

def dfs(node):
    if node not in visited:
        visited.add(node)
        for neighbor in sorted(graph[node]):
            dfs(neighbor)

dfs(1)
print(len(visited) - 1)