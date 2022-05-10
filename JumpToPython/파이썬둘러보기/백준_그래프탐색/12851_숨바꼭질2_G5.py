"""
 *packageName    : 
 * fileName       : 12851_숨바꼭질2_G5
 * author         : ipeac
 * date           : 2022-05-09
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-05-09        ipeac       최초 생성
 """

# 수빈 > 동생 찾기 n : 수빈 k : 동생
from collections import deque

n, k = map(int, input().split())
MAX_SIZE = 100001

graph = [[MAX_SIZE, 0] for _ in range(MAX_SIZE)]

queue = deque()
queue.append(n)

graph[n][0] = 0
graph[n][1] = 1

while queue:
      x = queue.popleft()
      
      for nx in [x * 2, x + 1, x - 1]:
            
            if 0 <= nx < MAX_SIZE:
                  
                  if graph[nx][0] == MAX_SIZE:
                        queue.append(nx)
                        graph[nx][0] = graph[x][0] + 1
                        graph[nx][1] = graph[x][1]
                  
                  elif graph[nx][0] == graph[x][0]:
                        graph[nx][1] += graph[x][1]

print(graph[k][0])
print(graph[k][1])
