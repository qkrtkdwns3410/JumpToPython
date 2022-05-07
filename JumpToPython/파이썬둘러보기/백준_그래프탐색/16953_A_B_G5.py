"""
 *packageName    : 
 * fileName       : 16953_A_B_G5
 * author         : jihye94
 * date           : 2022-05-07
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-05-07        jihye94       최초 생성
 """
import sys
from collections import deque

A, B = map(int, input().split())

queue = deque()
queue.append((A, 1))

while queue:
      x, t = queue.popleft()
      
      if x == B:
            print(t)
            sys.exit()
      
      if x * 2 <= B:
            queue.append((x * 2, t + 1))
      
      x = int(str(x) + "1")
      if x <= B:
            queue.append((x, t + 1))
print(-1)
