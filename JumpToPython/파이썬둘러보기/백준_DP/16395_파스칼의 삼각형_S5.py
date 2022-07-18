"""
 *packageName    : 
 * fileName       : 16395_파스칼의 삼각형_S5
 * author         : jihye94
 * date           : 2022-07-18
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-07-18        jihye94       최초 생성
 """
import sys

input = sys.stdin.readline

pascal = [[1 for _ in range(i)] for i in range(1, 31)]
for i in range(2, 30):
    for j in range(1, i):
        pascal[i][j] = pascal[i - 1][j - 1] + pascal[i - 1][j]

n, k = map(int, input().split())
print(pascal[n - 1][k - 1])
