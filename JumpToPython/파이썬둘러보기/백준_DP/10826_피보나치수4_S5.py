"""
 *packageName    : 
 * fileName       : 10826_피보나치수4_S5
 * author         : jihye94
 * date           : 2022-07-16
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-07-16        jihye94       최초 생성
 """
import sys

input = sys.stdin.readline


def dp(n):
    if n == 0:
        print(0)
        sys.exit(0)
    
    if n == 1 or n == 2:
        print(1)
        sys.exit(0)
    
    dp_arr = [0, 1, 1]
    
    for i in range(3, n + 1):
        
        dp_arr.append(dp_arr[i - 1] + dp_arr[i - 2])
        if i == n:
            print(dp_arr[i])
            sys.exit(0)




dp(int(input()))
