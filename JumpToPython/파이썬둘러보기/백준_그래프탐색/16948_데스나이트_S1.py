"""
 *packageName    : 
 * fileName       : 16948_데스나이트_S1
 * author         : jihye94
 * date           : 2022-06-25
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-06-25        jihye94       최초 생성
 """
# 체크판의 크기 n
from collections import deque

dx, dy = [-2, -2, 0, 0, 2, 2], [-1, 1, -2, 2, -1, 1]

n = int(input())
# 데스 나이트가 (r1, c1)에서 (r2, c2)로 이동
r1, c1, r2, c2 = map(int, input().split())

graph = [[0] * n for _ in range(n)]
print("graph : %s " % graph)

def bfs():
      visitied = [[0] * n for _ in range(n)]
      visitied[r1][c1] = 1
      q = deque()
      q.append((r1, c1))
      
      while q:
            x, y = q.popleft()
            
            for i in range(6):
                  nx, ny = x + dx[i], y + dy[i]
                  
                  if 0 <= nx < n and 0 <= ny < n and not visitied[nx][ny]:
                        visitied[nx][ny] = visitied[x][y] + 1
                        q.append((nx, ny))
                        if nx == r2 and ny == c2:
                              return visitied[nx][ny] - 1
      return -1



print(bfs())
