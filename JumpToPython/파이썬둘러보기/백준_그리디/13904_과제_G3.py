"""
 *packageName    : 
 * fileName       : 13904_과제_G3
 * author         : qkrtk
 * date           : 2022-04-04
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-04-04        qkrtk       최초 생성
 """
from heapq import *


def Solution(n, homework_list):
      ans = []
      homework_list = sorted(homework_list, key=lambda x: x[0])
      print("homework_list : %s " % homework_list)
      
      for i in range(n):
            heappush(ans, homework_list[i][1])
            
            print("1ans : %s " % ans)
            
            if len(ans) > homework_list[i][0]:
                  heappop(ans)
                  
                  print("22ans : %s " % ans)
      
      print(sum(ans))










Solution(7, [[4, 60], [4, 40], [1, 20], [2, 50], [3, 30], [4, 10], [6, 5]])

n = int(input())
homework_list_input = []
for _ in range(n):
      homework_list_input.append(list(map(int, input().split())))

Solution(n, homework_list_input)
