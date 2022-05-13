"""
 *packageName    :
 * fileName       : 14226_이모티콘_G5
 * author         : jihye94
 * date           : 2022-05-13
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-05-13        jihye94       최초 생성
 """
# 이모티콘 S의 개수
from collections import deque


s = int(input())

# x = 초기 이모티콘의 개수  y  = 클립보드
q = deque()
q.append((1, 0))
visited = dict()
visited[(1, 0)] = 0

while q:
      e, c = q.popleft()
      if e == s:
            print(visited[(s, c)])
            break
      
      # 화면에 있는 모든 이모티콘을 복사
      if (e, e) not in visited.keys():
            visited[(e, e)] = visited[(e, c)] + 1
            q.append((e, e))
      
      # 화면에 있는 모든 이모티콘 중 하나를 삭제
      if (e - 1, c) not in visited.keys():
            visited[(e - 1, c)] = visited[(e, c)] + 1
            q.append((e - 1, c))
      
      #  클립보드에 있는 이모티콘을 붙여넣기
      if (e + c, c) not in visited.keys():
            visited[(e + c, c)] = visited[(e, c)] + 1
            q.append((e + c, c))
