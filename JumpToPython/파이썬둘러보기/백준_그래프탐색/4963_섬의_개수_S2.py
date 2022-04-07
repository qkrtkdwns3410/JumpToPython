"""
 *packageName    : 
 * fileName       : 4963_섬의_개수_S2
 * author         : qkrtk
 * date           : 2022-04-07
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-04-07        qkrtk       최초 생성
 """
import sys

sys.setrecursionlimit(10 ** 6)


# DFS

def dfs(x, y):
      if x >= w or x < 0 or y >= h or y < 0 or graph[y][x] == 0:
            return False
      
      graph[y][x] = 0
      visited[y][x] = 1
      
      dfs(x + 1, y)
      dfs(x - 1, y)
      dfs(x - 1, y + 1)
      dfs(x + 1, y + 1)
      dfs(x + 1, y - 1)
      dfs(x - 1, y - 1)
      dfs(x, y + 1)
      dfs(x, y - 1)





while True:
      w, h = map(int, input().split())
      if w == 0 or h == 0:
            sys.exit(0)
      graph = []
      for _ in range(h):
            width = [list(map(int, input().split()))]
            graph.extend(width)
      
      cnt = 0
      
      visited = [[0] * w for _ in range(h)]
      
      for i in range(h):
            for j in range(w):
                  
                  if visited[i][j] == 0 and graph[i][j] == 1:
                        dfs(j, i)
                        cnt += 1
      print(cnt)
