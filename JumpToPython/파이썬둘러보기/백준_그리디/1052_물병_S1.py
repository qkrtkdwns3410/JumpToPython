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
      print("==========================================")
      N, K = map(int, ex1.split())

      purchased_water_bottle_cnt = 0

      while bin(N).count('1') > K:
            idx = bin(N)[::-1].index('1')
            purchased_water_bottle_cnt += 2 ** idx
            N += 2 ** idx

      print(purchased_water_bottle_cnt)



a = sys.stdin.readline()
Solution(a)

# Solution("3 1")
# Solution("13 2")
# Solution("1001 999")
Solution("1000000 5")
# Solution("9 2")
