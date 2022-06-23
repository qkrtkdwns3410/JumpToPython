"""
 *packageName    : 
 * fileName       : 12761_돌다리_S1
 * author         : ipeac
 * date           : 2022-06-23
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-06-23        ipeac       최초 생성
 """
from collections import deque


def bfs(graph, n):
      visited = [0] * 100001
      q = deque()
      q.append(n)
      visited[n] = 1
      
      while q:
            x = q.popleft()
            
            for i in range(8):
                  if i < 6:
                        nx = x + dx[i]
                  else:
                        nx = x * dx[i]
                  
                  if 0 <= nx <= 100000 and visited[nx] == 0:
                        graph[nx] = graph[x] + 1
                        visited[nx] = 1
                        q.append(nx)



# 스카이콩콩 a | b 의 힘 , 동규와 주미의 현재 위치 n m
a, b, n, m = map(int, input().split())

dx = [1, -1, a, b, -a, -b, a, b]

graph = [0] * 100001
bfs(graph, n)
print(graph[m])
