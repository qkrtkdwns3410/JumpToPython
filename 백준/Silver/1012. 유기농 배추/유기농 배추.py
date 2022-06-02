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
