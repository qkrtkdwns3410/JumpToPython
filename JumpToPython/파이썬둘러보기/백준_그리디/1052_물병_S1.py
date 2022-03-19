"""
 *packageName    : 
 * fileName       : 1052_물병_S1
 * author         : qkrtk
 * date           : 2022-03-19
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-03-19        qkrtk       최초 생성
 """
import sys


def Solution(ex1):
      bottle, one_move_able_bottle = list(map(int, ex1.split()))
      need_liter = 0
      plus_need_liter = 1
      if bottle < one_move_able_bottle:
            print(0)
            return
      while True:

            if bottle == one_move_able_bottle:
                  print(need_liter)

                  break
            elif one_move_able_bottle > bottle > 0:

                  if one_move_able_bottle % 2 != 0:
                        while plus_need_liter > need_liter:
                              plus_need_liter //= 2
                        need_liter -= plus_need_liter

                  print(need_liter)
                  break
            elif bottle <= 0:
                  print(-1)
                  return

            if bottle % 2 != 0:
                  need_liter += plus_need_liter
                  plus_need_liter *= 2

                  bottle += 1
                  bottle //= 2
            else:
                  bottle //= 2
                  plus_need_liter *= 2


a = sys.stdin.readline()
Solution(a)

# Solution("3 1")
# Solution("13 2")
# Solution("4 1")
# Solution("1000000 5")
