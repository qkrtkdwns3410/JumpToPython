"""
 *packageName    : 
 * fileName       : 1325_효율적인해킹_S1
 * author         : ipeac
 * date           : 2022-06-14
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-06-14        ipeac       최초 생성
 """
from collections import deque

def bfs(node_list, R):
      q = deque()
      visited = [False for _ in range(N + 1)]
      
      q.append(R)
      visited[R] = True
      cnt = 1
      while q:
            x = q.popleft()
            for j in node_list[x]:
                  if not visited[j]:
                        q.append(j)
                        visited[j] = True
                        cnt += 1
      
      return cnt

N, M = map(int, input().split())

# 노드의 리스트
node_list = [[] for _ in range(N + 1)]

for i in range(M):
      u, v = map(int, input().split())
      # 단방향 노드임
      node_list[v].append(u)

max_value = -1

result = []

for i in range(1, N + 1):
      # 컴퓨터마다 노드 탐색
      res = bfs(node_list, i)
      if res > max_value:
            result = [i]
            max_value = res
      elif res == max_value:
            result.append(i)
print(*result)
