from collections import deque


def bfs(R):
      global visited
      
      q = deque()
      q.append(R)
      visited[R] = 1
      while q:
            x = q.popleft()
            
            for w in graph[x]:
                  if not visited[w]:
                        visited[w] = visited[x] + 1
                        q.append(w)






n, m, = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)

for i in range(m):
      A_i, B_i = map(int, input().split())
      graph[A_i].append(B_i)
      graph[B_i].append(A_i)

bfs(1)
max_value = max(visited)
print(visited.index(max_value), max_value - 1, visited.count(max_value))