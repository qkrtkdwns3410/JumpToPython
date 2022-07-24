n = int(input())
n_arr = list(map(int, input().rstrip().split()))
n_arr.sort()
result = []
if len(n_arr) % 2 == 0:
    print(n_arr[len(n_arr) // 2 - 1])
else:
    print(n_arr[len(n_arr) // 2])