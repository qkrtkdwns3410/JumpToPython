"""
 *packageName    : 
 * fileName       : 1049_기타줄_S4
 * author         : ipeac
 * date           : 2022-03-24
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-03-24        ipeac       최초 생성
 """
import heapq
import sys


def Solution(n, m, guitar_list):
      print("==========================================")
      print("n : %s " % n)
      print("m : %s " % m)
      print("guitar_list : %s " % guitar_list)
      
      six_list = sorted(guitar_list, key=lambda x: x[0])
      one_list = sorted(guitar_list, key=lambda x: x[1])
      print("six_list : %s " % six_list)
      print("one_list : %s " % one_list)
      
      result = 0
      
      if six_list[0][0] <= one_list[0][1] * 6:
            result = six_list[0][0] * (n // 6) + (n % 6) * one_list[0][1]
      else:
            result = n * one_list[0][1]
      
      if result > six_list[0][0] * (n // 6 + 1):
            result = six_list[0][0] * (n // 6 + 1)
      print(result)


n, m, = map(int, sys.stdin.readline().split())
guitar_list = []
for _ in range(m):
      guitar_list.append(list(map(int, sys.stdin.readline().split())))

Solution(n, m, guitar_list)

# Solution(4, 2, [[12, 3], [15, 4]])


Solution(10, 3, [[20, 8], [40, 7], [60, 4]])
Solution(15, 1, [[100, 40]])
Solution(17, 1, [[12, 3]])
Solution(7, 2, [[10, 3], [12, 2]])
