from collections import deque

dx = [3, 2, 1]

def bfs(n):
      q = deque()
      q.append((n, [n]))
      visited = [0] * (n + 1)
      
      while q:
            num, node_list = q.popleft()
            if num == 1:
                  print(len(node_list) - 1)
                  print(*node_list)
                  return
            if not visited[num]:
                  visited[num] = 1
                  if num % 3 == 0:
                        q.append((num // 3, node_list + [num // 3]))
                  if num % 2 == 0:
                        q.append((num // 2, node_list + [num // 2],))
                  q.append((num - 1, node_list + [num - 1]))



n = int(input())

bfs(n)
