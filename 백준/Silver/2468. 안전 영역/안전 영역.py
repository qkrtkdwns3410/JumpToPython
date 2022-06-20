from collections import deque

dx, dy = [0, 0, 1, -1], [-1, 1, 0, 0]
cnt = 0

def bfs(visited, x, y, depth):
      visited[x][y] = True
      
      q = deque()
      q.append((x, y))
      
      while q:
            x1, y1 = q.popleft()
            
            for i in range(4):
                  nx, ny = x1 + dx[i], y1 + dy[i]
                  
                  if nx < 0 or ny < 0 or nx >= n or ny >= n:
                        continue
                  if graph[nx][ny] > depth and not visited[nx][ny]:
                        visited[nx][ny] = True
                        q.append((nx, ny))


n = int(input())
max_num = -1

graph = []
for i in range(n):
      graph.append(list(map(int, input().split())))
      for j in range(n):
            if graph[i][j] > max_num:
                  max_num = graph[i][j]

max_value = float('-inf')

for k in range(max_num):
      visited = [[False] * n for _ in range(n)]
      cnt = 0
      for i in range(n):
            for j in range(n):
                  if graph[i][j] > k and not visited[i][j]:
                        bfs(visited, i, j, k)
                        cnt += 1
      if max_value < cnt:
            max_value = cnt

print(max_value)