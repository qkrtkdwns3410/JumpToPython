import sys

input = sys.stdin.readline

n = int(input())
n_arr = list(map(int, input().split()))

n_arr_sorted = sorted(set(n_arr))
dict = {n_arr_sorted[i]: i for i in range(len(n_arr_sorted))}

for i in n_arr:
    print(dict[i], end=' ')