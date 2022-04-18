"""
 *packageName    : 
 * fileName       : 7562_나이트_이동_S1
 * author         : ipeac
 * date           : 2022-04-18
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-04-18        ipeac       최초 생성
 """
from collections import deque

dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [-1, -2, -2, -1, 1, 2, 2, 1]

# 테스트 케이스
n = int(input())
for _ in range(n):
      # 체스판의 크기 x y
      l = int(input())
      
      graph = []
      for i in range(l):
            # 그래프 만들기
            graph.append([0] * l)
      queue = deque()
      
      # 나이트의 초기 위치
      x, y = map(int, input().split())
      
      # 나이트 목표 위치
      w, z = map(int, input().split())
      
      queue.append((x, y))
      
      while queue:
            x, y = queue.popleft()
            if x == w and y == z:
                  break
            for i in range(8):
                  nx = x + dx[i]
                  ny = y + dy[i]
                  if nx < 0 or ny < 0 or nx >= l or ny >= l:
                        continue
                  if graph[nx][ny] == 0:
                        graph[nx][ny] = graph[x][y] + 1
                        queue.append((nx, ny))
      print(graph[w][z])
