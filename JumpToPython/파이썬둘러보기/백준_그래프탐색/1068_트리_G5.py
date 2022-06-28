"""
 *packageName    : 
 * fileName       : 1068_트리_G5
 * author         : jihye94
 * date           : 2022-06-28
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-06-28        jihye94       최초 생성
 """

def dfs(v):
      graph[v] = -2
      
      for i in range(n):  # 전체 트리의 반복
            if v == graph[i]:  # 지울 노드가 graph[i]에 존재 > graph[i]는 v의 자식
                  dfs(i)  # i의 자식도 삭제

n = int(input())  # 트리 노드의 개수 n

graph = list(map(int, input().split()))

remove_node = int(input())

dfs(remove_node)
cnt = 0
print("graph : %s " % graph)

for i in range(n):
      if graph[i] != -2 and i not in graph:
            print("i : %s " % i)
            
            cnt += 1

print(cnt)
