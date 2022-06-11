import sys

sys.setrecursionlimit(100000)

def dfs(graph, v, visited, nodes_cnt):
      global cnt
      # 방문처리
      visited[v] = True
      # 노드 방문 순서 기록
      nodes_cnt[v] = cnt
      cnt += 1
      # 연결된 노드로 이동할 수 있도록 !
      for i in graph[v]:
            if not visited[i]:
                  dfs(graph, i, visited, nodes_cnt)

N, M, R = (map(int, input().split()))

# 그래프
graph = [[] for _ in range(N + 1)]

visited = [False for _ in range(N + 1)]
nodes_cnt = [0 for _ in range(N + 1)]

for _ in range(M):
      x, y = map(int, input().split())
      # 무방향 그래프이기에 양방향으로 갈 수 있다는 점 유의 x y 위치에 표시
      graph[x].append(y)
      graph[y].append(x)
# 인접 정점은 오름차순으로 방문하기에 sort처리
for i in graph:
      i.sort()

cnt = 1
dfs(graph, R, visited, nodes_cnt)

for index, value in enumerate(nodes_cnt):
      if index >= 1:
            print(value)