"""
 *packageName    : 
 * fileName       : 14502_연구소_G5
 * author         : ipeac
 * date           : 2022-07-12
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-07-12        ipeac       최초 생성
 """
import copy
import sys
from collections import deque

input = sys.stdin.readline

dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]

n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

answer = 0


def bfs():
    q = deque()
    
    graph_c = copy.deepcopy(graph)
    for i in range(n):
        for j in range(m):
            if graph_c[i][j] == 2:
                q.append([i, j])
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m:
                if graph_c[nx][ny] == 0:
                    graph_c[nx][ny] = 2
                    q.append([nx, ny])
    
    global answer
    cnt = 0
    
    for i in range(n):
        for j in range(m):
            if graph_c[i][j] == 0:
                cnt += 1
    
    answer = max(answer, cnt)


def wall(x, start_row, start_col):
    if x == 3:
        bfs()
        
        return
    
    for i in range(start_row, n):
        for j in range(start_col, m):
            # 그래프가 0이라면 해당 위치에 벽을 살살 세워본다
            if graph[i][j] == 0:
                graph[i][j] = 1
                wall(x + 1, i, j + 1)
                graph[i][j] = 0
        start_col = 0


wall(0, 0, 0)
print(answer)
