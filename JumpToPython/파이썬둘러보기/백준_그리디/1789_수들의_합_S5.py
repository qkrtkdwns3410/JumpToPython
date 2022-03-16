"""
 *packageName    : 
 * fileName       : 1789_수들의_합_S5
 * author         : ipeac
 * date           : 2022-03-17
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-03-17        ipeac       최초 생성
 """


def Solution(ex1):
      print("ex1 : %s " % ex1)
      ex1 = int(ex1)

      init_num = 1
      count_result = 0

      while ex1 >= 0:
            if ex1 - init_num < 0:
                  break

            else:
                  ex1 -= init_num

            init_num += 1
            count_result += 1
            print("ex1 : %s " % ex1)

      print(count_result)


a = input()
Solution(a)

Solution("200")
print("==========================================")
