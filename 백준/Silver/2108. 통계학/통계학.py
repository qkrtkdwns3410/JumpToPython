import sys

input = sys.stdin.readline
# n 홀수
import collections

n = int(input())
n_arr = list(int(input()) for _ in range(n))

# 오름차순 정렬
n_arr.sort()

# 산술평균
average_num = round(sum(n_arr) / n)
print(average_num)

# 중앙값
median_num = n_arr[n // 2]
print(median_num)

count = collections.Counter(n_arr)
# 최빈값
if n > 1:
    counter_num = sorted(count.most_common(n=2), key=lambda x: (x[1], x[0]))
    print(counter_num.pop()[0])
else:
    print(count.most_common(n=1).pop()[0])

# 범위 출력
range_num = abs(max(n_arr) - min(n_arr))
print(range_num)