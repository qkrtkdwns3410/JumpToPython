import collections
import sys

input = sys.stdin.readline

n = int(input())

n_arr = list(int(input()) for _ in range(n))

most_common_one = sorted(collections.Counter(n_arr).items(), key=lambda x: (-x[1], x[0]))
print(most_common_one.pop(0)[0])
