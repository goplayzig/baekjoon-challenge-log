# 11724 연결 요소의 개수
import sys

sys.setrecursionlimit(10000)

N, M = map(int, sys.stdin.readline().split())
graph = {i: [] for i in range(1, N + 1)}

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

visited = set()
def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)

connected = 0

for node in range(1, N + 1):
    if node not in visited:
        dfs(node)
        connected += 1

print(connected)

        
