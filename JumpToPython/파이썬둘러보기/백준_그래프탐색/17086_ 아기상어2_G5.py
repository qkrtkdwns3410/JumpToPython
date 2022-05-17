"""
 *packageName    : 
 * fileName       : 17086_ 아기상어2_G5
 * author         : ipeac
 * date           : 2022-05-17
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-05-17        ipeac       최초 생성
 """
from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[-1] * m for _ in range(n)]

dx = (-1, -1, -1, 0, 0, 1, 1, 1)
dy = (-1, 0, 1, -1, 1, 1, 0, -1)

q = deque()
for i in range(n):
      for j in range(m):
            if graph[i][j] == 1:
                  q.append((i, j))
                  visited[i][j] = 0
ans = 0

while q:
      x, y = q.popleft()
      for k in range(8):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == -1:
                  visited[nx][ny] = visited[x][y] + 1
                  ans = max(ans, visited[nx][ny])
                  q.append((nx, ny))
print(ans)
