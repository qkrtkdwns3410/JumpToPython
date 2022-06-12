# 격자의 세로 M, 가로 N
from collections import deque

def bfs(x, y):
      q = deque([(x, y)])
      visited[x][y] = True
      while q:
            x, y = q.popleft()
            for j in range(4):
                  nx, ny = dx[j] + x, dy[j] + y
                  if 0 > nx or 0 > ny or nx >= M or ny >= N or visited[nx][ny] or graph[nx][ny] != 0:
                        continue
                  if graph[nx][ny] == 0:
                        if not visited[nx][ny]:
                              q.append((nx, ny))
                              visited[nx][ny] = True


dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]

# M 줄(세로) N (가로 칸)
M, N = map(int, input().split())

graph = [list(map(int, list(input()))) for _ in range(M)]
visited = [[False] * N for _ in range(M)]

for i in range(N):
      if graph[0][i] == 0:
            bfs(0, i)
print("YES" if True in visited[-1] else "NO")