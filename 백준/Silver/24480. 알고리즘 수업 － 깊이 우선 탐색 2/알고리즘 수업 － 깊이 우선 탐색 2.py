import sys

sys.setrecursionlimit(10 ** 5)
# 정점의 수 N , 간선의 수 M , 시작 정점 R
N, M, R = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for i in range(M):
      # 간선의 정보 담기
      u, v = map(int, input().split())
      graph[u].append(v)
      graph[v].append(u)
# 정점 방문 카운트는 내림차순!
for i in graph:
      i.sort(reverse=True)

# 방문여부
visited = [False] * (N + 1)
# 정점 방문 카운트
nodes_cnt = [0] * (N + 1)
cnt = 1

def dfs(graph, visited, R, nodes_cnt):
      global cnt
      
      nodes_cnt[R] = cnt
      cnt += 1
      
      visited[R] = True
      for i in graph[R]:
            if not visited[i]:
                  dfs(graph, visited, i, nodes_cnt)


dfs(graph, visited, R, nodes_cnt)

for index, value in enumerate(nodes_cnt):
      if index >= 1:
            print(value)