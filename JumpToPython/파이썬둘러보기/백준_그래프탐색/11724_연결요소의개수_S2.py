"""
 *packageName    : 
 * fileName       : 11724_연결요소의개수_S2
 * author         : qkrtk
 * date           : 2022-04-07
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-04-07        qkrtk       최초 생성
 """
import sys

sys.setrecursionlimit(10 ** 4)

# n 정점 m 간선의 개수
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
result = 0

for _ in range(m):
      u, v = map(int, input().split())
      graph[u].append(v)
      graph[v].append(u)

print("graph : %s " % graph)


def dfs(v):
      visited[v] = True
      for i in graph[v]:
            if not visited[i]:
                  dfs(i)


for i in range(1, n + 1):
      if not visited[i]:
            dfs(i)
            result += 1
print(result)
