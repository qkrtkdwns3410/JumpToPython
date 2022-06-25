"""
 *packageName    : 
 * fileName       : 12852_1로만들기2_S1
 * author         : jihye94
 * date           : 2022-06-25
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-06-25        jihye94       최초 생성
 """
from collections import deque

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
