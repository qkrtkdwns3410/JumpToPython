"""
 *packageName    : 
 * fileName       : 1260_DFSBFS_S2
 * author         : ipeac
 * date           : 2022-04-06
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-04-06        ipeac       최초 생성
 """
from collections import deque

n, m, v = map(int, input().split())
graph = [[0 for i in range(n + 1)] for j in range(n + 1)]
visited_d = [0] * (n + 1)
visited_b = [0] * (n + 1)

for i in range(m):
      line = list(map(int, input().split()))
      graph[line[0]][line[1]] = 1
      graph[line[1]][line[0]] = 1


def dfs(graph, v, visited_d):
      visited_d[v] = 1
      print(v, end=" ")
      for i in range(len(graph[v])):
            if visited_d[i] != 1 and graph[v][i] == 1:
                  dfs(graph, i, visited_d)


def bfs(graph, v, visited_b):
      visited_b[v] = 1
      queue = deque([v])
      
      while queue:
            v = queue.popleft()
            print(v, end=" ")
            
            for i in range(len(graph[v])):
                  if visited_b[i] != 1 and graph[v][i] == 1:
                        queue.append(i)
                        visited_b[i] = 1


dfs(graph, v, visited_d)
print()
bfs(graph, v, visited_b)
