"""
 *packageName    : 
 * fileName       : 1743_음식물 피하기_S1
 * author         : jihye94
 * date           : 2022-04-29
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-04-29        jihye94       최초 생성
 """
from collections import deque


def bfs(i, j):
      print("==========================================")
      queue.append((i, j))
      visited[i][j] = 1
      print("visited : %s " % visited)
      
      t = 1
      while queue:
            x, y = queue.popleft()
            for k in range(4):
                  nx, ny = x + dx[k], y + dy[k]
                  if 1 <= nx <= N and 1 <= ny <= M and graph[nx][ny] == 1 and visited[nx][ny] == 0:
                        visited[nx][ny] = 1
                        print("visited : %s " % visited)
                        
                        t += 1
                        queue.append((nx, ny))
      
      print("t : %s " % t)
      return t


N, M, K = map(int, input().split())
graph = [[0] * (M + 1) for _ in range(N + 1)]
print("graph : %s " % graph)

for i in range(K):
      x, y = map(int, input().split(" "))
      graph[x][y] = 1
visited = [[0] * (M + 1) for _ in range(N + 1)]
print("graph : %s " % graph)

queue = deque()
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

ans = 0

for i in range(1, N + 1):
      for j in range(1, M + 1):
            if graph[i][j] == 1 and visited[i][j] == 0:
                  res = bfs(i, j)
                  if res > ans:
                        ans = res

print(ans)
