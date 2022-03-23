"""
 *packageName    : 
 * fileName       : 2437_저울_G3
 * author         : qkrtk
 * date           : 2022-03-23
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-03-23        qkrtk       최초 생성
 """
import sys


def Solution(n, weight_list):
      weight_list.sort()
      result = 0
      
      for i in range(n):
            if result + 1 >= weight_list[i]:
                  result += weight_list[i]
            
            else:
                  break
      
      print(result + 1)



n = int(input())
temp_list = list(map(int, sys.stdin.readline().split()))

Solution(n, temp_list)
