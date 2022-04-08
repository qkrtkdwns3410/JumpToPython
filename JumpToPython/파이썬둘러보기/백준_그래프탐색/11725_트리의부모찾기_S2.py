"""
 *packageName    : 
 * fileName       : 11725_트리의부모찾기_S2
 * author         : qkrtk
 * date           : 2022-04-08
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-04-08        qkrtk       최초 생성
 """
import sys

input = sys.stdin.readline

sys.setrecursionlimit(10 ** 5)

# n 정점이자 노드루트의 개수
n = int(input())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
for _ in range(n - 1):
      x, y = map(int, input().split())
      graph[x].append(y)
      graph[y].append(x)

print("graph : %s " % graph)


def dfs(v):
      for i in graph[v]:
            if not visited[i]:
                  visited[i] = v
                  dfs(i)


dfs(1)

for i in range(2, n + 1):
      print(visited[i])
