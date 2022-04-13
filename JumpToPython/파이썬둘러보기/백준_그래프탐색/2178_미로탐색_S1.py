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
import collections

n, m = map(int, input().split())
graph = [list(map(int, ' '.join(input()).split())) for _ in range(n)]
print("graph : %s " % graph)

# 이동
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

Q = collections.deque([(0, 0)])
result = 0

while Q:
      x, y = Q.popleft()
      for i in range(4):
            
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m:
                  if graph[nx][ny] == 1:
                        
                        graph[nx][ny] = graph[x][y] + 1
                        Q.append((nx, ny))

print(graph[n - 1][m - 1])
