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
 
 1. 배추밭의 가로길이 m
 2. 배추밭의 세로길이 n
 3. 배추가 심어져 있는 위치의 개수 k
 """
import sys

sys.setrecursionlimit(10 ** 6)

t = int(input())


def dfs(x, y):
      if x >= m or x < 0 or y >= n or y < 0 or graph[y][x] == 0:
            return False
      graph[y][x] = 0
      visited[y][x] = 1
      
      dfs(x + 1, y)
      dfs(x - 1, y)
      dfs(x, y + 1)
      dfs(x, y - 1)



# m x좌표 n y좌표  k 줄
for i in range(t):
      m, n, k = map(int, input().split())
      
      graph = [[0] * m for _ in range(n)]
      post = []
      for i in range(k):
            x, y = map(int, input().split())
            graph[y][x] = 1
      cnt = 0
      visited = [[0] * m for i in range(n)]
      
      for i in range(n):
            for j in range(m):
                  
                  if visited[i][j] == 0 and graph[i][j] == 1:
                        dfs(j, i)
                        cnt += 1
      print(cnt)
