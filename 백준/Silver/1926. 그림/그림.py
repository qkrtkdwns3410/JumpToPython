from collections import deque

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
cnt = 0

def bfs(graph, visited, x, y):
      width = 1
      global cnt
      
      visited[x][y] = True
      
      q = deque()
      q.append((x, y))
      
      while q:
            x1, y1 = q.popleft()
            
            for i in range(4):
                  nx, ny = x1 + dx[i], y1 + dy[i]
                  if 0 > nx or 0 > ny or n <= nx or m <= ny or visited[nx][ny]:
                        continue
                  if graph[nx][ny] and not visited[nx][ny]:
                        width += 1
                        q.append((nx, ny))
                        visited[nx][ny] = True
      cnt += 1
      return width





n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [([0] * m) for _ in range(n)]

max_value = float('-inf')
for i in range(n):
      for j in range(m):
            if graph[i][j] == 1 and not visited[i][j]:
                  res = bfs(graph, visited, i, j)
                  if max_value < res:
                        max_value = res
print(cnt)
print('0' if cnt == 0 else max_value)