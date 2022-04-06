"""
 *packageName    : 
 * fileName       : 1202_보석_도둑_G2
 * author         : ipeac
 * date           : 2022-03-27
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-03-27        ipeac       최초 생성
 """
import heapq
import sys


def Solution(jew_list, max_weight_list):
      max_weight_list.sort()
      jew_list.sort()
      print("max_weight_list : %s " % max_weight_list)
      print("jew_list : %s " % jew_list)
      
      res = 0
      
      temp = []
      
      for bag in max_weight_list:
            while jew_list and bag >= jew_list[0][0]:
                  heapq.heappush(temp, -jew_list[0][1])
                  heapq.heappop(jew_list)
            
            if temp:
                  res += heapq.heappop(temp)
            elif not jew_list:
                  break
      print(-res)


# Solution(2, 1, [[5, 10], [100, 100]], [11])
# Solution(3, 2, [[1, 65], [5, 23], [2, 99]], [10, 2])
# Solution(2, 2, [[5, 5], [5, 5]], [1, 10])

n, k = map(int, sys.stdin.readline().split())

jew_list = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
max_weight_list = [int(sys.stdin.readline()) for _ in range(k)]
Solution(jew_list, max_weight_list)
