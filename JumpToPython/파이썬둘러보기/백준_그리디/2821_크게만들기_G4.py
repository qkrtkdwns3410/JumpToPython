"""
 *packageName    : 
 * fileName       : 2821_크게만들기_G4
 * author         : qkrtk
 * date           : 2022-04-03
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-04-03        qkrtk       최초 생성
 """
import sys


def Solution(n, k, number_list):
      print("==========================================")
      print("n : %s " % n)
      print("k : %s " % k)
      number_list = list(map(int, number_list))
      
      result = []
      del_num = k
      for i in range(n):
            while del_num > 0 and result:
                  if result[len(result) - 1] < number_list[i]:
                        result.pop()
                        del_num -= 1
                  else:
                        break
            result.append(number_list[i])
      
      print("number_list : %s " % number_list)
      for i in range(n - k):
            print(result[i], end="")








Solution(4, 2, "1924")
Solution(7, 3, "1231234")
Solution(10, 4, "4177252841")
n, k = map(int, sys.stdin.readline().split())
num = str(input())
Solution(n, k, num)
