"""
 *packageName    : 
 * fileName       : 2178_미로탐색_S1
 * author         : ipeac
 * date           : 2022-04-13
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-04-13        ipeac       최초 생성
 """
from collections import deque

def bfs(i, j):
      queue.append((i, j))
      visited[i][j] = 1
      while queue:
            x, y = queue.popleft()
            for k in range(4):
                  nx, ny = x + dx[k], y + dy[k]
                  if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0 and graph[nx][ny] == 1:
                        queue.append((nx, ny))
                        visited[nx][ny] = visited[x][y] + 1


N, M = map(int, input().split())
graph = [list(map(int, input())) for _ in range(N)]

visited = [[0] * M for _ in range(N)]

queue = deque()
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

bfs(0, 0)

print(visited[-1][-1])
