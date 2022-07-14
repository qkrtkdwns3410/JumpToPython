import sys
from collections import deque

input = sys.stdin.readline

# 인접한 칸 이동가능
dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]



def bfs(i, j):
    q = deque()
    
    # 체크했는지 확인
    
    q.append([i, j])
    
    # 연합 국가 save
    union = [[i, j]]
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                if r >= abs(a[x][y] - a[nx][ny]) >= l:
                    q.append([nx, ny])
                    visited[nx][ny] = 1
                    union.append([nx, ny])
    
    return union


if __name__ == '__main__':
    answer = 0
    # n* n 크기의 땅 | r 행 c 열 나라 A[r][c] 명이 살고있음
    n, l, r = map(int, input().split())
    # n 개  줄 인구수
    a = [list(map(int, input().split())) for _ in range(n)]
    
    # 인구차이  l 이상 r 이하 라면 국경선 오픈 ||
    # 인구 이동이 없을 때까지 지속된다.
    while True:
        person_moving = False
        
        visited = [list([0] * n) for _ in range(n)]
        
        for i in range(n):
            for j in range(n):
                if visited[i][j] == 0:
                    visited[i][j] = 1
                    union = bfs(i, j)
                    if len(union) > 1:
                        person_moving = True
                        union_pol = sum([a[x][y] for x, y in union]) // len(union)
                        for x, y in union:
                            a[x][y] = union_pol
        
        if not person_moving:
            break
        # 하루가 흘렀다.  > 연합을 해제하고 모든 국경선을 닫는다. || 변경된 그래프 적용 및 visited 초기화
        answer += 1
    print(answer)
