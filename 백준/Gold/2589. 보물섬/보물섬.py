import sys
from collections import deque

input = sys.stdin.readline
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]


def bfs(x, y):
    visited = [list([0] * b) for _ in range(a)]
    
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < a and 0 <= ny < b:
                if graph[nx][ny] == 'L' and not visited[nx][ny]:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))
    
    return max(map(max, visited))



# 보물 지도의 세로 크기 a , 가로의 크기 b
a, b = map(int, input().split())

graph = [list(input()) for _ in range(a)]
cnt = []
for xindex, xline in enumerate(graph):
    for yindex, value in enumerate(xline):
        if value == 'L':
            cnt.append(bfs(xindex, yindex))

print(max(cnt) - 1)