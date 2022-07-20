# n ; 듣도 못한 사람 m ; 보도 못한 사람
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

no_listen_arr = [input().rstrip() for _ in range(n + m)]

no_listen_arr.sort()
result = 0
result_name = []
pre_name = no_listen_arr[0]
for i in range(1, len(no_listen_arr)):
    if pre_name == no_listen_arr[i]:
        result += 1
        result_name.append(pre_name)
    else:
        pre_name = no_listen_arr[i]

print(result)

for name in list(dict.fromkeys(result_name)):
    print(name)