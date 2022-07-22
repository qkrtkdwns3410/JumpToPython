import sys

input = sys.stdin.readline

n = int(input())
n_arr = list(map(int, input().split()))
n_arr.sort()
x = int(input())


# data는 오름차순으로 정렬된 리스트
def binary_search_recursion(target, left, right):
    if left > right:
        return 0

    mid = (left + right) // 2

    if n_arr[mid] == target:
        return 1
    elif n_arr[mid] > target:
        return binary_search_recursion(target, left, mid - 1)
    elif n_arr[mid] < target:
        return binary_search_recursion(target, mid + 1, right)


count = 0
for num in n_arr:
    # 해당값 제곱값이 10 이면 5 를 이진탐색시 같은 5를 반환.. 카운트되면 안됨
    if num ** 2 == x:
        continue
    count += binary_search_recursion(x - num, 0, n - 1)
print(count // 2)