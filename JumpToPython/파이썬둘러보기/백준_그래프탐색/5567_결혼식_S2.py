"""
 *packageName    : 
 * fileName       : 5567_결혼식_S2
 * author         : ipeac
 * date           : 2022-06-12
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-06-12        ipeac       최초 생성
 """

def dfs(graph, visited):
      global cnt
      cnt += 1
      
      pass

# 동기의 수 n
n = int(input())

# 리스트의 길이 m
m = int(input())

# 그래프
graph = [[] for _ in range(n)]
visited = [[False] for _ in range(n)]
print("graph : %s " % graph)

for _ in range(m):
      u, v = map(int, input().split())
      graph[u].append(v)
      graph[v].append(u)

print("graph : %s " % graph)
cnt = 0

for i in graph:
      if not visited[i]:
            dfs(graph, visited)
