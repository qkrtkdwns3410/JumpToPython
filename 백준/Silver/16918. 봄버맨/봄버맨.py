from collections import deque

dx, dy = [-1, 1, 0, 0, 0], [0, 0, -1, 1, 0]
q = deque()

def time_set(time):
    global visited, graph
    for index, line in enumerate(graph):
        for index2, line_o in enumerate(line):
            if line_o == 'O' and visited[index][index2] == -10:
                # 초기에 설치된 폭탄
                visited[index][index2] = time

def fill_graph(time):
    global visited, graph
    for index, line in enumerate(graph):
        for index2, line_o in enumerate(line):
            if line_o == '.' and visited[index][index2] == -10:
                # 폭탄 새로 세팅
                visited[index][index2] = time
                graph[index][index2] = 'O'

def boom(time):
    boom_lst = []
    for i in range(r):
        for j in range(c):
            # 폭탄이 존재.. 하고 시간이 설치 시간 + 3 과 동일하다면
            if graph[i][j] == 'O' and time == visited[i][j] + 3:
                # 현재 위치기준으로 좌우상하 탐색
                for k in range(5):
                    nx, ny = i + dx[k], j + dy[k]
                    
                    if 0 <= i + dx[k] < r and 0 <= j + dy[k] < c:
                        boom_lst.append([nx, ny])
    for x, y in boom_lst:
        graph[x][y], visited[x][y] = '.', -10



# r : 가로 줄 , c : 세로 줄 , n : n 초 후 격자판의 상태 출력
r, c, n = map(int, input().split())

graph = [list(map(str, input())) for _ in range(r)]

visited = [[-10] * c for _ in range(r)]

for i in range(n + 1):
    if i == 0:
        # 초기 폭탄 카운트 세팅
        time_set(0)
    elif i == 1:
        
        pass
    elif i % 2 == 0:
        # 폭탄 새로 채우기
        fill_graph(i)
        # 타이머 설정
        time_set(i)
    elif i % 2 != 0:
        # 폭탄을 터뜨립니다.
        boom(i)
for index, line in enumerate(graph):
    for index2, line_o in enumerate(line):
        print(line_o, end='')
    print()