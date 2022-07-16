import sys

input = sys.stdin.readline

def dp(n):
    result = 0
    if n == 0:
        print(4)
        sys.exit()
    if n == 1:
        print(6)
        sys.exit()
    if n == 2:
        print(10)
        sys.exit()
    
    dp_arr = [1, 1, 2]
    
    for i in range(3, n + 1):
        dp_arr.append(dp_arr[i - 1] + dp_arr[i - 2])
        if i == n:
            result = dp_arr[i] * 3 + dp_arr[i - 1] * 2 + dp_arr[i - 2] * 2 + dp_arr[i - 3]
    
    return result


print(dp(int(input()) - 1))