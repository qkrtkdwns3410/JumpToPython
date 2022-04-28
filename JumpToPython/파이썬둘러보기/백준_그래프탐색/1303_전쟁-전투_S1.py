"""
 *packageName    : 
 * fileName       : 1303_전쟁-전투_S1
 * author         : ipeac
 * date           : 2022-04-28
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-04-28        ipeac       최초 생성
 """
from collections import deque

def bfs():
      queue.append((i, j))
      visited[i][j] = 1
      t = 1
      while queue:
            x, y = queue.popleft()
            for k in range(4):
                  nx, ny = x + dx[k], y + dy[k]
                  if 0 <= nx < M and 0 <= ny < N and graph[nx][ny] == graph[i][j] and visited[nx][ny] == 0:
                        visited[nx][ny] = 1
                        queue.append((nx, ny))
                        t += 1
      return t



# N : 가로 M : 세로
N, M = map(int, input().split())
graph = [list(map(str, input())) for _ in range(M)]
print("graph : %s " % graph)
visited = [[False] * N for _ in range(M)]
print("visited : %s " % visited)

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
queue = deque()
B, W = 0, 0

for i in range(M):
      for j in range(N):
            if visited[i][j] == 0:
                  ans = bfs()
                  if graph[i][j] == 'W':
                        W += ans ** 2
                  else:
                        B += ans ** 2
print(W, B)
