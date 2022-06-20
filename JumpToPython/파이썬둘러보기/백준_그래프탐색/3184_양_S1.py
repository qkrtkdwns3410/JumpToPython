"""
 *packageName    : 
 * fileName       : 3184_양_S1
 * author         : jihye94
 * date           : 2022-06-20
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-06-20        jihye94       최초 생성
 """
from collections import deque

dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]

def bfs(i, j, visited):
      global global_o_cnt
      global global_v_cnt
      
      # 늑대 카운트
      v_cnt = 0
      # 양 카운트
      o_cnt = 0
      
      q = deque()
      q.append((i, j))
      
      visited[i][j] = True
      if graph[i][j] == 'v':
            v_cnt += 1
      if graph[i][j] == 'o':
            o_cnt += 1
      while q:
            x, y = q.popleft()
            
            for i in range(4):
                  nx, ny = x + dx[i], y + dy[i]
                  if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny] and graph[nx][ny] != '#':
                        if graph[nx][ny] == 'v':
                              v_cnt += 1
                        if graph[nx][ny] == 'o':
                              o_cnt += 1
                        q.append((nx, ny))
                        visited[nx][ny] = True
      if o_cnt > v_cnt:
            global_o_cnt += o_cnt
      elif o_cnt <= v_cnt:
            global_v_cnt += v_cnt


r, c = map(int, input().split())
graph = []
global_o_cnt = 0
global_v_cnt = 0
visited = [[False] * c for _ in range(r)]

#  || . >> 빈필드 || # >> 울타리 || o >> 양 || v >> 늑대
for i in range(r):
      graph.append(list(map(str, input())))

for i in range(r):
      for j in range(c):
            if not visited[i][j]:
                  bfs(i, j, visited)

print(global_o_cnt, global_v_cnt)
