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

def dfs(graph, visited, R, depth):
      # 친구의 친구까지만 구해야합니다. 0 (친구) 1 (친구의 친구)
      if depth >= 2:
            return
      
      print("graph : %s " % graph)
      
      for i in graph[R]:
            if not visited[i]:
                  visited[i] = True
            
            # 방문하지 않은 노드인 경우 dfs 진행.(친구가 중복되어 카운트되면 안됨)  - 그리고 depth도 +1 시켜줘서 친구의 친구까지만 구할 수 있도록
            dfs(graph, visited, i, depth + 1)

# 동기의 수 n
n = int(input())

# 리스트의 길이 m
m = int(input())

# 그래프
graph = [[] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]
print("graph : %s " % graph)

for _ in range(m):
      u, v = map(int, input().split())
      graph[u].append(v)
      graph[v].append(u)
      print("graph : %s " % graph)

# 상근이 학번 1은 무조건  vitised
visited[1] = True
# 상근이의 학번은 1입니다.  기본 depth 0
dfs(graph, visited, 1, 0)
print("graph : %s " % graph)
print("visited : %s " % visited)

cnt = 0
for i in visited:
      if i:
            cnt += 1
print(cnt - 1)
