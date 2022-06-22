"""
 * packageName    :
 * fileName       : 11403_경로찾기_S1
 * author         : jihye94
 * date           : 2022-04-23
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-04-23        jihye94       최초 생성
 """
from collections import deque

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

def bfs(x):
      queue = deque()
      queue.append(x)
      check = [0 for _ in range(n)]
      
      while queue:
            q = queue.popleft()
            
            for i in range(n):
                  if check[i] == 0 and graph[q][i] == 1:
                        queue.append(i)
                        check[i] = 1
                        visited[x][i] = 1

for i in range(0, n):
      bfs(i)

for i in visited:
      print(*i)
