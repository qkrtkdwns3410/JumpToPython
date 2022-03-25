"""
 *packageName    : 
 * fileName       : 1439_뒤집기_S5
 * author         : ipeac
 * date           : 2022-03-24
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-03-24        ipeac       최초 생성
 """
import sys


def Solution(s):
      print("==========================================")
      print("s : %s " % s)
      temp = 0
      switch = False
      cnt = 0
      for index, num in enumerate(s):
            if index == 0:
                  temp = num
                  print("temp : %s " % temp)
            
            else:
                  if temp != num:
                        if switch:
                              continue
                        cnt += 1
                        switch = True
                  elif temp == num and switch:
                        switch = False
      print(cnt)


n = list(input())
Solution(n)
# Solution([0, 0, 0, 1, 1, 0, 0])
# Solution([1, 1, 1, 1, 1])
# Solution([0, 0, 0, 0, 0, 0, 0, 1])
# Solution([1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1])
# Solution([1, 1, 1, 0, 1, 1, 0, 1])
