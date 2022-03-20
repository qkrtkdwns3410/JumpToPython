"""
 *packageName    : 
 * fileName       : 2212_센서_G5
 * author         : qkrtk
 * date           : 2022-03-20
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-03-20        qkrtk       최초 생성
 """
import sys


def Solution(list_x):
      list_cha = []
      if k > n:
            print(0)
            return
      
      for index in range(n - 1):
            list_cha.append(list_x[index + 1] - list_x[index])
      list_cha.sort(reverse=True)
      for _ in range(k - 1):
            list_cha.pop(0)
      print(sum(list_cha))







n = int(input())
k = int(input())
list_n = []
list_n.extend(input().split(" "))
list_n = list(map(int, list_n))

list_n.sort()

Solution(list_n)
