#
#
#
#
#
#
#
#
#
from collections import deque


def bfs(v):
      print("v : %s " % v)
      visited = [False] * n
      queue = deque([(v, 0)])  # 사람의 번호와 친구와의 관계
      
      visited[v] = True
      cnt = 0
      
      while queue:
            a, b = queue.popleft()
            
            # 친구와의 관계가 2이상이면 생각하지 않는다.
            if b >= 2:
                  continue
            
            # 반복문을 통해 탐색하지 않은 사람이고 그 사람이 친구가 있는지 확인
            for i in range(n):
                  if not visited[i] and graph[a][i] == "Y":
                        cnt += 1
                        visited[i] = True
                        queue.append([i, b + 1])
      
      return cnt





n = int(input())
graph = [list(map(str, input())) for _ in range(n)]
print("graph : %s " % graph)

res = 0

for i in range(n):
      res = max(res, bfs(i))

print(res)
