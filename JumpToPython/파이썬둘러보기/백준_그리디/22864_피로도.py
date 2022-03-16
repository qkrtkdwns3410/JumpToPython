"""
 *packageName    : 
 * fileName       : 22864_피로도
 * author         : ipeac
 * date           : 2022-03-16
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-03-16        ipeac       최초 생성
 """
import sys

"""
A ; 하루에 한 시간 일하면 피로도 쌓이는..
B ;  하루에 한 시간 일할 때 처리할 수 있는 일
C ; 한 시간 쉰다면 피로도 얼마나 줄어드는 지  ;; 피로도가 음수로 내려가면 0으로 변경
M ; 피로도는 M을 넘지않도록!

하루는 24시간입니다.!
"""

A, B, C, M = map(int, input().split())
p = 0
work = 0
for _ in range(24):
      if p + A <= M:  # 일할 수 있으면
            p += A
            work += B
      else:
            if p - C < 0:
                  p = 0
            else:
                  p -= C
print(work)

# a = input()
# solution(a)
#
# solution("5 3 2 10")
# print("==========================================")
# solution("10 5 1 10")
# print("==========================================")
# solution("11 5 1 10")
