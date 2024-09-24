n = int(input())
tree = [[] for _ in range(n+1)]
parent = [0] * (n+1) 
for _ in range(n-1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)
def dfs_stack(start):
    stack = [start]
    parent[start] = -1 
    while stack:
        node = stack.pop()
        for child in tree[node]:
            if parent[child] == 0: 
                parent[child] = node  
                stack.append(child) 
dfs_stack(1)
for i in range(2, n+1):
    print(parent[i])
