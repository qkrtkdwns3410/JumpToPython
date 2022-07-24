import bisect

T = int(input())
for _ in range(T):
    n, m = map(int, input().split())

    a = sorted(list(map(int, input().split())))
    b = sorted(list(map(int, input().split())))

    result = 0
    for value in a:
        result += bisect.bisect(b, value - 1)
    print(result)