from collections import deque

def bfs():
      visited = [0 for _ in range(n + 1)]
      q = deque()
      q.append([home_x, home_y])
      
      while q:
            x, y = q.popleft()
            # 집 - 페스티벌 거리 1000 이하인 경우 한방에감
            if abs(x - festival_x) + abs(y - festival_y) <= 1000:
                  print('happy')
                  return
                  # 편의점의 개수만큼 반복 // 해당 편의점을 방문했는지 체크
            for i in range(n):
                  if not visited[i]:
                        gs25_x, gs25_y = gs25[i]
                        if abs(x - gs25_x) + abs(y - gs25_y) <= 1000:
                              q.append([gs25_x, gs25_y])
                              visited[i] = 1
      print('sad')




# 테스트 케이스의 수
t = int(input())
for case in range(t):
      
      hp = 20
      
      # 맥주를 파는 편의점의 개수 n
      n = int(input())
      # 상근집
      home_x, home_y = map(int, input().split())
      
      gs25 = []
      
      #  편의점  좌표
      for i in range(n):
            x, y = map(int, input().split())
            gs25.append([x, y])
      
      # 락 페스티벌
      festival_x, festival_y, = map(int, input().split())
      
      bfs()