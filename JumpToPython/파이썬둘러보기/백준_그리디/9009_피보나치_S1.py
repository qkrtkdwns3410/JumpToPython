"""
 *packageName    : 
 * fileName       : 9009_피보나치_S1
 * author         : qkrtk
 * date           : 2022-03-19
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-03-19        qkrtk       최초 생성
 """
import sys
from functools import lru_cache



def Solution(test_data):
      x = 0
      result_list = []
      while fibo(x) <= test_data:
            x += 1

            if fibo(x) > test_data:
                  x -= 1
                  result_list.insert(0, fibo(x))
                  test_data -= fibo(x)
                  x = 0

                  pass
            if test_data <= 0:
                  for num in result_list:
                        print(num, end=" ")
                  print()
                  return


@lru_cache(maxsize=None)
def fibo(x):
      if x == 0:
            return 0
      elif x == 1 or x == 2:
            return 1
      else:
            return fibo(x - 1) + fibo(x - 2)



T = int(sys.stdin.readline())

for _ in range(T):
      a = int(sys.stdin.readline())
      Solution(a)
