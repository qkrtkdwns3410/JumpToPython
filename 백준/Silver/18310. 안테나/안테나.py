# 집의 수
n = int(input())
n_arr = list(map(int, input().split()))

n_arr.sort()
print(n_arr[(n - 1) // 2])
