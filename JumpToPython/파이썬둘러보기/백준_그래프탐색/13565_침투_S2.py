"""
 *packageName    : 
 * fileName       : 13565_침투_S2
 * author         : qkrtk
 * date           : 2022-04-08
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-04-08        qkrtk       최초 생성
 """
# bfs 로 풀이해 보겠음.
m, n = map(int, input().split())
graph = []
visited = [[False] * n]
for _ in range(m):
      graph.append(list(map(int, input())))

print("graph : %s " % graph)


def dfs(v):
      visited[v] = True
      
      for i in graph[v]:
            if not visited[i]:
                  dfs(i)


dfs(1)
