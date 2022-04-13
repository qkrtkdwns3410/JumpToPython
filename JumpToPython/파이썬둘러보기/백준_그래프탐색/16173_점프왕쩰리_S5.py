"""
 *packageName    : 
 * fileName       : 16173_점프왕쩰리_S4
 * author         : ipeac
 * date           : 2022-04-13
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-04-13        ipeac       최초 생성
 """
import sys

sys.setrecursionlimit(10 ** 5)


def dfs(x, y):
      if x < 0 or x >= n or y < 0 or y >= n:
            return False
      
      if visited[x][y]:
            return False
      
      if graph[x][y] == -1:
            print("HaruHaru")
            sys.exit(0)
      
      visited[x][y] = True
      
      dfs(x + graph[x][y], y)
      dfs(x, y + graph[x][y])
      
      return True








n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [list([False] * n) for _ in range(n)]

print("graph : %s " % graph)
print("visited : %s " % visited)

if dfs(0, 0):
      print("Hing")
