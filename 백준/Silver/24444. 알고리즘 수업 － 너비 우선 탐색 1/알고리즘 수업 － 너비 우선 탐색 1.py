import sys
from collections import deque
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n, m, r = map(int, input().split()) # 정점의 수, 간선의 수, 시작 정점
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1) # 방문 순서 저장. 0이면 방문 X

c = 1 # 순서
def bfs(graph, start, visited):
    global c
    queue = deque([start])
    visited[start] = c # 방문하면 순서 나타내기
    
    while queue:
        v = queue.popleft()
        for i in graph[v]: # 인접 노드 중
            if visited[i] == 0: # 방문하지 않은 노드 큐에 추가
                queue.append(i)
                c += 1 # 순서+1
                visited[i] = c

# m개의 연결된 간선 정보 입력받기
for i in range(m):
    a, b = (map(int, input().split()))
    graph[a].append(b)
    graph[b].append(a)
# print(graph)

for i in range(n+1): # 인접노드 정보 오름차순 정렬
    graph[i].sort()
# print(graph)

bfs(graph, r, visited)

for i in range(1, n+1):
    print(visited[i])