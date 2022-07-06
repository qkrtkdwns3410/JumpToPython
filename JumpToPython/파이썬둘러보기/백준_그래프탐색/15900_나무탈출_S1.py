"""
 *packageName    : 
 * fileName       : 15900_나무탈출_S1
 * author         : ipeac
 * date           : 2022-07-05
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-07-05        ipeac       최초 생성
 """
# from collections import deque
#
# def bfs(f_num, graph):
#     q = deque()
#
#     visited = [0 for _ in range(n + 1)]
#     dist = [0 for _ in range(n + 1)]
#
#     q.append(f_num)
#     visited[1] = 1
#     print("graph : %s " % graph)
#
#     while q:
#         x = q.popleft()
#
#         for v in graph[x]:
#             if not visited[v]:
#                 q.append(v)
#                 visited[v] = 1
#                 # 노드 to 루트노드
#                 # 부모 노드에 +1
#                 dist[v] = dist[x] + 1
#
#     print("visited : %s " % visited)
#     answer = 0
#     # 리프 노드의 탐색
#     for i in range(2, n + 1):
#         if len(graph[i]) == 1:
#             answer += dist[i]
#             print("answer : %s " % answer)
#     if answer % 2 == 0:
#         print("NO")
#     else:
#         print("YES")
#
#
#
#
# # n  정점의 개수
# n = int(input())
# graph = [[] for _ in range(n + 1)]
# # n-1 줄 까지 트리의 간선정보 a b 사이에 간선이 존재한다는 의미
# for i in range(n - 1):
#     a, b = map(int, input().split())
#
#     graph[a].append(b)
#     graph[b].append(a)
#
# bfs(1, graph)
from collections import deque

n = int(input())

graph = [[] for _ in range(n + 1)]
visit = [0] * (n + 1)
distance = [0] * (n + 1)

# 그래프 만들기
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(v, graph):
    queue = deque()
    queue.append(v)
    visit[v] = 1
    while queue:
        v = queue.popleft()
        for g in graph[v]:
            if visit[g] != 1:
                queue.append(g)
                visit[g] = 1
                # 노드와 루트 노드까지 사이 거리
                # 자신의 부모 노드에 + 1을 하면 됨
                distance[g] = distance[v] + 1
    answer = 0
    # 리프 노드 찾기
    # 루트 노드를 제외하기 위해 범위는 2~n+1
    # 리프노드의 거리 합 구하기
    for i in range(2, n + 1):
        if len(graph[i]) == 1:
            answer += distance[i]
    # 합이 짝수면 지고, 홀수면 이긴다.
    if answer % 2 != 0:
        print("Yes")
    else:
        
        print("No")


bfs(1, graph)
