"""
 *packageName    : 
 * fileName       : 14496_그대,그머가 되어_S1
 * author         : jihye94
 * date           : 2022-07-06
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-07-06        jihye94       최초 생성
 """
from collections import deque
from sys import stdin

input = stdin.readline


def bfs(a, graph):
    visited = [0 for _ in range(n + 1)]
    q = deque([(a, 0)])
    visited[a] = 1
    
    while q:
        x, cnt = q.popleft()
        if x == b:
            print(cnt)
            return
        for line in graph[x]:
            if not visited[line]:
                q.append((line, cnt + 1))
                visited[line] = 1
    
    print(-1)


# 바꾸려고 하는 문자 a b
a, b = map(int, input().split())
# 전체 문자 수 n, 치환 가능한 문자쌍의 수 m
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for i in range(m):
    u, v = map(int, input().split())
    if u == v:
        continue
    graph[v].append(u)
    graph[u].append(v)
bfs(a, graph)


# from sys import stdin
# from collections import deque
#
# input = stdin.readline
#
# s, e = map(int, input().split())
# n, m = map(int, input().split())
# adj_list = [[] for _ in range(n + 1)]
#
# for _ in range(m):
#     a, b = map(int, input().split())
#     adj_list[a].append(b)
#     adj_list[b].append(a)
#
#
# def solv():
#     visited = [False] * (n + 1)
#
#     q = deque([(s, 0)])
#     visited[s] = True
#
#     while q:
#         now, cnt = q.pop()
#
#         if now == e:
#             print(cnt)
#             return
#
#         for nxt in adj_list[now]:
#             if not visited[nxt]:
#                 visited[nxt] = True
#                 q.appendleft((nxt, cnt + 1))
#     print(-1)
#
#
# solv()
