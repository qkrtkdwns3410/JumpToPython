"""
 *packageName    : 
 * fileName       : 1010_다리놓기_G5
 * author         : ipeac
 * date           : 2022-07-15
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-07-15        ipeac       최초 생성
 """
import sys

input = sys.stdin.readline
# 테스트 케이스
T = int(input())

for _ in range(T):
    # 서 n || 동 m
    n, m, = map(int, input().split())
    dp = [list([0] * (m + 1)) for _ in range(n + 1)]
    for i in range(1, m + 1):
        dp[1][i] = i
    
    for i in range(2, n + 1):
        for j in range(1, m + 1):
            dp[i][j] = dp[i][j - 1] + dp[i - 1][j - 1]
    print(dp[n][m])
