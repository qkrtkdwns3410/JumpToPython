"""
 *packageName    : 
 * fileName       : __init__.py
 * author         : ipeac
 * date           : 2022-04-18
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-04-18        ipeac       최초 생성
 """
from collections import deque
import sys

r = sys.stdin.readline

n, m = map(int, r().split())

array = [[] for _ in range(n + 1)]


def bfs(v):
      q = deque([v])
      print("array : %s " % array)
      visited = [False] * (n + 1)
      visited[v] = True
      cnt = 1
      while q:
            v = q.popleft()
            print("visited : %s " % visited)
            for node in array[v]:
                  if not visited[node]:
                        q.append(node)
                        visited[node] = True
                        cnt += 1
      
      return cnt

for _ in range(m):
      a, b = map(int, r().split())
      array[b].append(a)

results = []
max_value = -1
for i in range(1, n + 1):
      result = bfs(i)
      print("result : %s " % result)
      if result > max_value:
            results = [i]
            max_value = result
      elif result == max_value:
            results.append(i)

print("results : %s " % results)
for re in results:
      print(re, end=" ")
