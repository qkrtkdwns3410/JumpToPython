"""
 *packageName    : 
 * fileName       : 2644_촌수계산_S2
 * author         : qkrtk
 * date           : 2022-04-08
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-04-08        qkrtk       최초 생성
 """
import sys

sys.setrecursionlimit(10 ** 6)
# n 정점
n = int(input())
a, b = map(int, input().split())
# m  간선의 개수
m = int(input())

graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
result = [0] * (n + 1)

for _ in range(m):
      x, y = map(int, input().split())
      graph[x].append(y)
      graph[y].append(x)


def dfs(v):
      visited[v] = True
      
      for i in graph[v]:
            if not visited[i]:
                  result[i] = result[v] + 1
                  dfs(i)


dfs(a)

if result[b] > 0:
      print(result[b])
else:
      print(-1)
