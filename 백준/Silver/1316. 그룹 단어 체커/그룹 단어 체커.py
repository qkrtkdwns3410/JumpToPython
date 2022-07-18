import sys

input = sys.stdin.readline

# 단어의 개수 n
n = int(input())
checker_cnt = 0

# n개 줄에 단어가 들어온다
for i in range(n):
    break_flag = False
    word = input()
    for index in range(len(word) - 1):
        # 단어의 전 인덱스 값이 현재 인덱스와 다르다면
        if word[index] != word[index + 1]:
            new_word = word[index + 1:]
            # 현재의 인덱스 값이 새로운 단어에 포함되어 있다면 그룹단어가 아니다.
            if word[index] in new_word:
                break_flag = True
    if break_flag:
        continue
    checker_cnt += 1

print(checker_cnt)