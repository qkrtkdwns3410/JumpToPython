from collections import deque


def bfs():
    q = deque()
    q.append(s)
    visited[s] = 1
    
    while q:
        xx = q.popleft()
        
        for i in range(2):
            nx = xx + dx[i]
            if 1 <= nx <= f:
                if not visited[nx]:
                    visited[nx] = visited[xx] + 1
                    q.append(nx)
                    if nx == g:
                        print(max(visited) - 1)
                        return
    print("use the stairs")



# f : 꼭대기 층수 || s : 현재 층 || g : 스타트링크 층 || u : 위로 U층을 가는 버튼 || d : 아래로 D층을 가는 버튼
f, s, g, u, d = map(int, input().split())
dx = [u, -d]
visited = [0] * (f + 1)

if s == g:
    print(0)
else:
    bfs()