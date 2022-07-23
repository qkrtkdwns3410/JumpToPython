import heapq

n = int(input())

q = []

for i in range(n):
    line = map(int, input().split())
    for value in line:
        if len(q) < n:
            heapq.heappush(q, value)
        else:
            if q[0] < value:
                heapq.heappushpop(q, value)

print(q[0])