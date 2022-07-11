import sys
from collections import deque

input = sys.stdin.readline

dx, dy = [0, 0, 1, -1], [-1, 1, 0, 0]


def bfs():
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                visited[nx][ny] = 1
                q.append([nx, ny])



# m : 가로 칸수 n : 세로 칸수
m, n = map(int, input().split())

graph = []

# 그래프 값 채워넣기
for x in range(n):
    graph.append(list(map(int, input().split())))

roti_sw = True

q = deque()
visited = [list(0 for _ in range(m)) for _ in range(n)]

for x in range(n):
    for y in range(m):
        if graph[x][y] == 1:
            q.append([x, y])
        else:
            roti_sw = False

# 토마토가 전부 익어있음 ;;
if roti_sw:
    print(0)
    sys.exit(0)

bfs()

for x, value in enumerate(graph):
    for y, value2, in enumerate(value):
        # 안익은 토마토가 존재한다면
        if graph[x][y] == 0:
            print(-1)
            sys.exit(0)

print(max(map(max, graph)) - 1)