"""
 *packageName    :
 * fileName       : 3-1. 거스름돈
 * author         : jihye94
 * date           : 2022-07-18
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-07-18        jihye94       최초 생성
 """
# 손님 거스름돈 n
n = int(input())
ans = 0

coin_arr = [500, 100, 50, 10]


def divide(value):
    global n
    global ans
    ans += n // value
    n -= value * (n // value)


for coin in coin_arr:
    if n >= coin:
        divide(coin)

print(ans)
