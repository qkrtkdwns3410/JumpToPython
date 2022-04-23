"""
 * packageName    :
 * fileName       : 11403_경로찾기_S1
 * author         : jihye94
 * date           : 2022-04-23
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-04-23        jihye94       최초 생성
 """
from collections import deque
import sys

input = sys.stdin.readline
N = int(input())  # 정점의 개수
G = [list(map(int, input().split())) for _ in range(N)]
result = [[0] * N for _ in range(N)]
lst = [[] for _ in range(N)]  # 간선 정보

# 간선 정보
for i in range(N):
      for j in range(N):
            if G[i][j] == 1:
                  lst[i].append(j)


def bfs(i):
      q = deque([i])
      while q:
            node = q.popleft()
            for v in lst[node]:
                  
                  if not visited[v]:
                        visited[v] = 1
                        q.append(v)
                        
                        if not result[i][v]:
                              result[i][v] = 1


for i in range(N):
      visited = [0] * N
      bfs(i)
      print(*result[i])
