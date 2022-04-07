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

sys.setrecursionlimit(10 * 6)


# DFS

def dfs(x, y):
      if x >= w or x < 0 or y >= h or y < 0 or graph[y][x] == 0:
            return False
      pass




while True:
      w, h = map(int, input().split())
