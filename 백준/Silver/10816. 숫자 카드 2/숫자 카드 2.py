# 가지고있는 수자 카드의 개수 N
import collections
import sys

input = sys.stdin.readline

n = int(input())
# 숫자 카드에 적혀있는 정수 (-10,000,000 ~ 10,000,000 )
n_arr = list(map(int, input().split()))

m = int(input())
# 상근이가 몇개를 가지고 있는 숫자카드인지 구해야할 M개의 정수
find_card_arr = list(map(int, input().split()))

# 각 수를 상근이가 몇 개 가지고 있는지

count = collections.Counter(n_arr)

for find_value in find_card_arr:
    print(count[find_value], end=" ")