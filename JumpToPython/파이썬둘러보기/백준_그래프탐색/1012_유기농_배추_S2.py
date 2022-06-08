"""
 *packageName    : 
 * fileName       : 1012_유기농_배추_S2
 * author         : ipeac
 * date           : 2022-04-06
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-04-06        ipeac       최초 생성
 

 """
# 방향성
from collections import deque

dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]

def bfs(x, y):
      q = deque()
      q.append((x, y))
      graph[x][y] = 0
      
      while q:
            # 해당 위치값 가져옴 ㅇㅇ (배추 잇는곳)
            x, y = q.popleft()
            # 4방향으로 회전시작
            for i in range(4):
                  nx, ny = x + dx[i], y + dy[i]
                  if nx < 0 or ny < 0 or ny >= N or nx >= M:
                        continue
                  if graph[nx][ny] == 1:
                        # 값을 0으로 만들고 해당 값 큐에 담아서 반복문 다시돔
                        graph[nx][ny] = 0
                        q.append((nx, ny))
      return

T = int(input())
for i in range(T):
      """
      1. 배추밭의 가로길이 m
      2. 배추밭의 세로길이 n
      3. 배추가 심어져 있는 위치의 개수 k
      """
      M, N, K = map(int, input().split())
      cnt = 0
      
      graph = [[0] * N for _ in range(M)]
      
      # 배추 위치 설정
      for j in range(K):
            x, y = map(int, input().split())
            graph[x][y] = 1
      
      # 지렁이 세팅
      for y in range(N):
            for x in range(M):
                  if graph[x][y] == 1:
                        bfs(x, y)
                        # 지렁이가 bfs 로 해당 칸을 다 돌면 한마리가 세팅되는거임 ㅇㅇ
                        cnt += 1
      print(cnt)
