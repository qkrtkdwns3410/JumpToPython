"""
 *packageName    : 
 * fileName       : 2606_바이러스_S3
 * author         : ipeac
 * date           : 2022-04-06
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-04-06        ipeac       최초 생성
 """
from collections import deque

n = int(input())  # 컴퓨터의 수
m = int(input())  # 연결된 컴퓨터 쌍의 수

# 인접리스트 graph 선언 및 입력받기
graph = [[0] * (n + 1) for _ in range(n + 1)]
visited = [0] * (n + 1)

for i in range(m):
      line = list(map(int, input().split()))
      graph[line[1]][line[0]] = 1
      graph[line[0]][line[1]] = 1


def dfs(start, graph, visited):
      visited[start] = 1
      com = deque()
      com.append(start)
      cnt = 0
      while com:
            v = com.popleft()
            
            for i in range(len(graph[v])):
                  if visited[i] != 1 and graph[v][i] == 1:
                        com.append(i)
                        visited[i] = 1
                        cnt += 1
      return cnt


dfs(1, graph, visited)

print(dfs(1, graph, visited))
