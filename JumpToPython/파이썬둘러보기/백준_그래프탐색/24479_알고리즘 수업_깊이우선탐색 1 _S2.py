"""
 *packageName    : 
 * fileName       : 24479_알고리즘 수업_깊이우선탐색 1 _S1
 * author         : ipeac
 * date           : 2022-06-08
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-06-08        ipeac       최초 생성
 """
import sys

# dfs 기본 재귀 제한 100000 설정때문에 재귀 제한을 100000으로 상향
sys.setrecursionlimit(10 ** 6)


def dfs(graph, v, R):
      pass

N, M, R = map(int, input().split())
print("N : %s " % N)

# 간선 연결 정보
graph = [[] for _ in range(N + 1)]
visited = [[False] for _ in range(N + 1)]
print("graph : %s " % graph)
print("visited : %s " % visited)

# 정점 방문순서 기록을 위한 배열
visited_cnts = [[0] for _ in range(N + 1)]

for _ in range(M):
      # 정점  u , 정점 v  양방향 간선
      u, v = map(int, input().split())
      
      # 양방향 간선이기에 > 해당 그래프 u v 위치마다 해당 노드 연결 정보를 담습니다.
      graph[u].append(v)
      graph[v].append(u)

print("graph : %s " % graph)
