"""
 *packageName    : 
 * fileName       : 14720_우유_축제
 * author         : ipeac
 * date           : 2022-03-16
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-03-16        ipeac       최초 생성
 """
import sys

count = 0
index = 0
last_milk_str = 0

N = int(input())

milkList = list(sys.stdin.readline().split())


def milkSeq():
      global count
      global index
      global last_milk_str
      for numStr in milkList:
            if numStr == str(last_milk_str):
                  count += 1
                  if last_milk_str == 2:
                        last_milk_str = 0
                  else:
                        last_milk_str += 1


milkSeq()
print(count)
