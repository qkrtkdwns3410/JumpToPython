"""
 *packageName    : 
 * fileName       : 10026_적록색약_G5
 * author         : ipeac
 * date           : 2022-07-11
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-07-11        ipeac       최초 생성
 """
import sys
from collections import deque

input = sys.stdin.readline

dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]



# 적록 색약인 경우
def bfs(a, b):
    q = deque()
    q.append([a, b])
    
    visited[a][b] = result
    
    while q:
        
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and graph[x][y] == graph[nx][ny]:
                visited[nx][ny] = 1
                q.append([nx, ny])



n = int(input())
graph = [list(map(str, input())) for _ in range(n)]
visited = [list([0] * n) for _ in range(n)]

print("graph : %s " % graph)

result = 0

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j)
            result += 1

print(result, end=' ')
result = 0

for index, line in enumerate(graph):
    for index2, value in enumerate(line):
        if value == "G":
            graph[index][index2] = "R"

visited = [list([0] * n) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j)
            result += 1
print(result)
