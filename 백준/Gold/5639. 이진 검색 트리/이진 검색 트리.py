import sys

sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline


def post_order(start, end):
    if start > end:
        return
    
    divisition = end + 1  # 나눌 위치
    for i in range(start + 1, end + 1):
        if graph[start] < graph[i]:
            divisition = i
            break
    post_order(start + 1, divisition - 1)  # 분할 왼쪽
    post_order(divisition, end)  # 분할 오른쪽
    print(graph[start])


graph = []
count = 0
# 10000이하 제약
while count <= 10000:
    try:
        num = int(input())
    except Exception:
        break
    graph.append(num)
    count += 1

post_order(0, len(graph) - 1)