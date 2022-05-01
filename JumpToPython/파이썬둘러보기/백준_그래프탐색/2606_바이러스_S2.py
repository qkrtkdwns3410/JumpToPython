"""
 *packageName    : 
 * fileName       : 2606_바이러스_S2
 * author         : jihye94
 * date           : 2022-04-29
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-04-29        jihye94       최초 생성
 """
from collections import deque

N = int(input())
visited = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]

# 노드의 개수
NN = int(input())
for i in range(NN):
      a, b = map(int, input().split())
      graph[a].append(b)
      graph[b].append(a)

visited[1] = 1
queue = deque([1])
while queue:
      x = queue.popleft()
      for i in range(len(graph[x])):
            
            if visited[graph[x][i]] == 0:
                  
                  queue.append(graph[x][i])
                  visited[graph[x][i]] = 1

print(sum(visited) - 1)
