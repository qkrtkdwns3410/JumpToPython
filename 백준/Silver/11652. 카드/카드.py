import collections
import sys

input = sys.stdin.readline

most_common_one = sorted(collections.Counter(list(int(input()) for _ in range(int(input())))).items(),
                         key=lambda x: (-x[1], x[0]))
print(most_common_one.pop(0)[0])