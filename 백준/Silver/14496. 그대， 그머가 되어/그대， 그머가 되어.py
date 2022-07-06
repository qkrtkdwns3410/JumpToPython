from sys import stdin
from collections import deque

input = stdin.readline

s,e = map(int, input().split())
n,m = map(int, input().split())
adj_list = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int, input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)

def solv():
    visited = [False]*(n+1)
    
    q = deque([(s,0)])
    visited[s] = True
    
    while q:
        now, cnt = q.pop()
        
        if now == e:
            print(cnt)
            return
        
        for nxt in adj_list[now]:
            if not visited[nxt]:
                visited[nxt] = True
                q.appendleft((nxt,cnt+1))
    print(-1)
solv()