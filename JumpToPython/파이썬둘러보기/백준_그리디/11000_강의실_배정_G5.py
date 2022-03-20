"""
 *packageName    : 
 * fileName       : 11000_강의실_배정_G5
 * author         : ipeac
 * date           : 2022-03-20
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-03-20        ipeac       최초 생성
 """
import sys


def Solution(ex1):
      print("==========================================")
      print("ex1 : %s " % ex1)
      pass


N = int(sys.stdin.readline())
class_time_list = []
for _ in range(N):

      s, t = map(int, sys.stdin.readline().split())
      class_time_list.append([s, t])

Solution(class_time_list)
