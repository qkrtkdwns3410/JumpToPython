"""
 *packageName    : 
 * fileName       : 13549_숨바꼭질3_G5
 * author         : ipeac
 * date           : 2022-05-10
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-05-10        ipeac       최초 생성
 """
from collections import deque

MAX_SIZE = 100001
n, k = map(int, input().split())

visitied = [False] * MAX_SIZE
dist = [-1] * MAX_SIZE

q = deque()
q.append(n)

visitied[n] = True
dist[n] = 0

while q:
      now = q.popleft()
      if now == k:
            print(dist[now])
            break
      
      if 0 <= now * 2 < MAX_SIZE and visitied[now * 2] == False:
            q.appendleft(now * 2)
            visitied[now * 2] = True
            dist[now * 2] = dist[now]
      
      if 0 < now + 1 < MAX_SIZE and visitied[now + 1] == False:
            q.append(now + 1)
            visitied[now + 1] = True
            dist[now + 1] = dist[now] + 1
      
      if MAX_SIZE > now - 1 >= 0 and visitied[now - 1] == False:
            q.append(now - 1)
            visitied[now - 1] = True
            dist[now - 1] = dist[now] + 1
