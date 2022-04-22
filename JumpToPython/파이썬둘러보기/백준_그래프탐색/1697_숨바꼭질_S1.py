"""
 *packageName    : 
 * fileName       : 1697_숨바꼭질_S1
 * author         : ipeac
 * date           : 2022-04-19
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-04-19        ipeac       최초 생성
 """
from collections import deque

n, k = map(int, input().split())
graph = [0 for _ in range(10 ** 6)]


def bfs(x):
      queue = deque([x])
      
      while queue:
            x = queue.popleft()
            if x == k:
                  return graph[x]
            
            for i in (x - 1, x + 1, 2 * x):
                  
                  if 0 <= i <= 100000 and graph[i] == 0:
                        graph[i] = graph[x] + 1
                        queue.append(i)


print(bfs(n))
