"""
 *packageName    : 
 * fileName       : 11060_점프 점프_S2
 * author         : ipeac
 * date           : 2022-07-06
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-07-06        ipeac       최초 생성
 """
import sys
from collections import deque

input = sys.stdin.readline


def bfs(graph):
    visited = [0 for _ in range(n)]
    visited[0] = 1
    q = deque()
    q.append(0)
    
    while q:
        x = q.popleft()
        # 1 ~ 해당 숫자 까지 점프가능
        for i in range(graph[x] + 1):
            jump_kan = x + i
            if not visited[jump_kan]:
                visited[jump_kan] = visited[x] + 1
                q.append(jump_kan)
                
                if jump_kan == len(graph) - 1:
                    print(visited[jump_kan] - 1)
                    return
    print(-1)


# 1X N 크기의 미로
n = int(input())

graph = list(map(int, input().split()))
if len(graph) == 1:
    print(0)
    sys.exit(0)
bfs(graph)
