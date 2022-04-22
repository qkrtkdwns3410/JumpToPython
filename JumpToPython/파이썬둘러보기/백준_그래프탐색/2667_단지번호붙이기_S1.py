"""
 *packageName    : 
 * fileName       : 2667_단지번호붙이기_S1
 * author         : ipeac
 * date           : 2022-04-19
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-04-19        ipeac       최초 생성
 """
from collections import deque


res = []
dx = [0, 1, -1, 0]
dy = [1, 0, 0, -1]

n = int(input())

graph = [list(map(int, input())) for _ in range(n)]


def bfs(a, b):
      queue = deque()
      
      # 초기
      queue.append((a, b))
      
      # 초기방문지점 방문처리
      graph[a][b] = 0
      
      count = 1
      
      while queue:
            x, y = queue.popleft()
            
            if x < 0 or y < 0 or x >= n or y >= n:
                  break
            
            for i in range(4):
                  nx = x + dx[i]
                  ny = y + dy[i]
                  
                  if nx < 0 or nx >= n or ny < 0 or ny >= n:
                        continue
                  
                  if graph[nx][ny] == 1:
                        graph[nx][ny] = 0
                        queue.append((nx, ny))
                        count += 1
      
      return count


for i in range(n):
      for j in range(n):
            if graph[i][j] == 1:
                  res.append(bfs(i, j))
print(len(res))
res.sort()
for num in res:
      print(num)
