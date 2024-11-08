import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
visited = [False for _ in range(n+1)]
s = int(input())

for x in list(map(int, input().split())):
    visited[x] = True

def dfs(s):
    visited[s] = True
    is_meet = not bool(graph[s])
    for u in graph[s]:
        if not visited[u] and dfs(u):
            return True
    return is_meet
    
print("Yes" if visited[1] or not dfs(1) else "yes")