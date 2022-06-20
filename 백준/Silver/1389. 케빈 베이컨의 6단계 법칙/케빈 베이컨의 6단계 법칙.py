from collections import deque

def bfs(node_list, R):
      visited = [0] * (N + 1)
      q = deque()
      q.append(R)
      visited[R] = 1
      
      while q:
            x = q.popleft()
            
            for i in node_list[x]:
                  if not visited[i]:
                        q.append(i)
                        visited[i] = visited[x] + 1
      return sum(visited)

#  유저의 수 N , 친구 관계의 수 M
N, M, = map(int, input().split())
node_list = [[] for _ in range(N + 1)]

for i in range(M):
      u, v = map(int, input().split())
      # 양방향 노드
      node_list[u].append(v)
      node_list[v].append(u)

min_value = float('inf')
result = []
for i in range(1, N + 1):
      res = bfs(node_list, i)
      if min_value > res:
            min_value = res
            result = [i]

print(*result)