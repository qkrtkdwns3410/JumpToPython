from collections import deque

dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

def bfs(x, y):
      q = deque()
      q.append((x, y))
      graph[x][y] = 1
      width = 1
      
      while q:
            y_value, x_value = q.popleft()
            
            for i in range(4):
                  ny, nx = y_value + dy[i], x_value + dx[i]
                  if (0 <= ny < M) and (0 <= nx < N) and not graph[ny][nx]:
                        width += 1
                        graph[ny][nx] = 1
                        q.append((ny, nx))
      return width

# M  가로   N 세로 K 사각형의 개수
M, N, K = map(int, input().split())
graph = [[0] * (N) for _ in range(M)]

for _ in range(K):
      # 왼쪽 아래 꼭짓점의 x, y좌표값 || 오른쪽 위 꼭짓점의 x, y좌표값
      x, y, x1, y1 = map(int, input().split())
      for i in range(y, y1):
            for j in range(x, x1):
                  graph[i][j] = 1
res = []
for i in range(M):
      for j in range(N):
            if not graph[i][j]:
                  result = bfs(i, j)
                  res.append(result)
res.sort()
print(len(res))
print(*res)
