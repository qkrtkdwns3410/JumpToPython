# 최단거리 파악
from collections import deque

def bfs(node_list, res, X):
      q = deque()
      q.append(X)
      
      res[X] = 0
      
      while q:
            x = q.popleft()
            for j in node_list[x]:
                  # 노드 리스트의 다음부분의 경로 지수가 0 인 경우 진행
                  if res[j] == -1:
                        # 해당 노드 경로 지수에 전 경로 값의 +1
                        res[j] = res[x] + 1
                        q.append(j)

# 도시의 개수 N , 도로의 개수  M , 거리 정보  K, 출발 도시의 번호 X
N, M, K, X = map(int, input().split())

node_list = [[] for _ in range(N + 1)]

res = [-1] * (N + 1)
for i in range(M):
      u, v = map(int, input().split())
      # 단뱡항 노드임
      node_list[u].append(v)

bfs(node_list, res, X)
check = False
for index, value in enumerate(res):
      if value == K:
            print(index)
            check = True

if not check:
      print(-1)
