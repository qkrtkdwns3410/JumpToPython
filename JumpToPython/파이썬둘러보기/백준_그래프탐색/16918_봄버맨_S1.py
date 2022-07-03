"""
 *packageName    : 
 * fileName       : 16918_봄버맨_S1
 * author         : ipeac
 * date           : 2022-07-03
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-07-03        ipeac       최초 생성
 """
from collections import deque

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
q = deque()

def bfs(graph, visited):
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx <= r and 0 <= ny <= c and not visited[nx][ny]:
                graph[nx][ny] = '.'


def simulate():
    global time, graph
    # 시간이 1초 인 경우
    if time == 1:
        pass
    # 3번의 경우에는 짝수초
    elif time % 2 == 0:
        graph = [['O'] * c for _ in range(r)]
    # 4번의 경우 홀수 초인 경우
    elif time % 2 == 1:
        pass




# r : 가로 줄 , c : 세로 줄 , n : n 초 후 격자판의 상태 출력
r, c, n = map(int, input().split())

graph = [list(map(str, input())) for _ in range(r)]
print("graph : %s " % graph)

visited = [[0] * c for _ in range(r)]
print("visited : %s " % visited)

time = 1
