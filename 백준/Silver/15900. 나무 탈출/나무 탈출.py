from collections import deque
n = int(input())

graph = [[] for _ in range(n+1)]
visit = [0] * (n+1)
distance = [0] * (n+1)

# 그래프 만들기
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
def bfs(v, graph) :
    queue = deque()
    queue.append(v)
    visit[v] = 1
    while queue :
        v = queue.popleft()
        for g in graph[v] :
            if visit[g] != 1 :
                queue.append(g)
                visit[g] = 1
                # 노드와 루트 노드까지 사이 거리
                # 자신의 부모 노드에 + 1을 하면 됨
                distance[g] = distance[v]+1
    answer = 0
    # 리프 노드 찾기
    # 루트 노드를 제외하기 위해 범위는 2~n+1
    # 리프노드의 거리 합 구하기
    for i in range(2, n+1) :
        if len(graph[i]) == 1 :
            answer += distance[i]
    # 합이 짝수면 지고, 홀수면 이긴다.
    if answer % 2 != 0 :
        print("Yes")
    else :
        print("No")
    

bfs(1, graph)