"""
 *packageName    : 
 * fileName       : 1783_병든_나이트_S4
 * author         : ipeac
 * date           : 2022-03-26
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-03-26        ipeac       최초 생성
 """


def Solution(y, x):
      print("==========================================")
      print("x : %s " % x)
      print("y : %s " % y)
      
      if y == 1:
            print(1)
      elif y == 2:
            print(min(4, ((x - 1) // 2) + 1))
      elif x < 6:
            print(min(4, x))
      else:
            print(x - 2)


# m, n = map(int, input().split())
# Solution(m, n)
Solution(100, 50)
Solution(1, 1)
Solution(17, 5)
Solution(2, 4)
Solution(20, 4)
