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

# 재귀 깊이 제한 파이썬 >> 1000 이라서 1000000 으로 설정해줘야합니다.
sys.setrecursionlimit(10 ** 6)

t = int(input())


# def dfs(x,y):
#       if x >=m or x<0 or y>=n or y<0 or
def dfs(x, y):
      pass


for i in range(t):
      m, n, k = map(int, input().split())
      
      graph = [[0] * m for i in range(n)]
      post = []
      for i in range(k):
            a, b = map(int, input().split())
            graph[b][a] = 1
      cnt = 0
      visited_d = [[0] * m for i in range(n)]
      
      for i in range(n):
            for j in range(m):
                  if visited_d[i][j] == 0 and graph[i][j] == 1:
                        dfs(j, i)
                        cnt += 1
      print(cnt)
