"""
 *packageName    : 
 * fileName       : 1260_DFS와BFS_S2
 * author         : qkrtk
 * date           : 2022-04-05
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-04-05        qkrtk       최초 생성
 """

from collections import deque

import sys

sys.setrecursionlimit(10 ** 6)

def dfs(v):
      print(v, end=" ")
      if v == m:
            return
      else:
            for i in range(1, n + 1):
                  if graph[v][i] == 1 and visited_D[i] is False:
                        visited_D[i] = True
                        dfs(i)



# 너비우선탐색
def bfs(v):
      queue = deque([])
      queue.append(v)
      while queue:
            x = queue.popleft()
            if visited_B[x] is False:
                  visited_B[x] = True
                  print(x, end=" ")
                  for i in range(1, n + 1):
                        if graph[x][i] == 1 and visited_B[i] is False:
                              queue.append(i)





n, m, v = map(int, input().split())
graph = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
      start, end = map(int, input().split())
      graph[start][end] = 1
      graph[end][start] = 1

visited_D = [False] * (n + 1)
visited_B = [False] * (n + 1)

visited_D[v] = True
dfs(v)
print()
bfs(v)
