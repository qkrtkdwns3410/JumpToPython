import sys

input = sys.stdin.readline

n = int(input())


def dp(n):
    # 5로 나눈 몫과 나머지
    d1, r1 = divmod(n, 5)
    while True:
        # 나머지가 2로 나눠진다면
        if r1 % 2 == 0:
            d2, r2 = divmod(r1, 2)
            print(d1 + d2)
            exit(0)
        # 2로 나눠지지 않는다면
        else:
            d1 -= 1
            r1 += 5
        if d1 < 0:
            print(-1)
            exit(0)

dp(n)