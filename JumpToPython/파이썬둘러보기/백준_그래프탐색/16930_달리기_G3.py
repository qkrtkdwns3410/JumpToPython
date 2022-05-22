"""
 *packageName    : 
 * fileName       : 16930_달리기_G3
 * author         : jihye94
 * date           : 2022-05-20
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-05-20        jihye94       최초 생성
 """
#  체육관의 크기 N M , 1초에 이동할 수 있는 칸의 최대 개수 K
from collections import deque

n, m, k = map(int, input().split())
print("n : %s " % n)
dx, dy = [-1, 0, 0, 1], [0, 1, -1, 0]

# N개 의 줄 체육관의 상태 :
#  마지막 줄 네 정수 x1, y1, x2, y2 두 칸은 서로 다른 칸, 항상 빈칸
graph = [list(input()) for _ in range(n)]
print("graph : %s " % graph)

x1, x2, y1, y2 = map(int, input().split())
visited = [[0] * m for _ in range(n)]

x1 -= 1
x2 -= 1
y1 -= 1
y2 -= 1

q = deque()
q.append((x1, x2))
visited[x1][x2] = 1

while q:
      x, y = q.popleft()
      for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
