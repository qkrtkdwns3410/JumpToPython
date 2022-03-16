"""
 *packageName    : 
 * fileName       : 2810_컵홀더
 * author         : ipeac
 * date           : 2022-03-16
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-03-16        ipeac       최초 생성
 """
import sys


def Solution(ex1):
      seat_list = ex1[1]

      result = 0

      if 'LL' in seat_list:
            result += seat_list.count('LL')
            result += seat_list.count('S')
            result += 1
      else:
            result += seat_list.count('S')

      print(result)


input_list = [input() for _ in range(2)]
Solution(input_list)
