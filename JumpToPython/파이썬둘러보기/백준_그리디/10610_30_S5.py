"""
 *packageName    : 
 * fileName       : 10610_30_S5
 * author         : qkrtk
 * date           : 2022-03-17
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-03-17        qkrtk       최초 생성
 """
"""
30의 배수는 3의 배수이면서 일의 자리가 0인 수이다.
3의 배수는 각 자리 숫자의 합이 3의 배수인 수이다.
"""


def Solution(ex1):
      print("ex1 : %s " % ex1)
      ex1_list = list(ex1)
      print("ex1_list : %s " % ex1_list)

      sum_each_num = 0

      if '0' not in ex1_list:
            print(-1)
            return
      elif '0' in ex1_list:
            ex1_list.sort(reverse=True)
            print("ex1_list : %s " % ex1_list)
            for index, num in enumerate(ex1_list):
                  if len(ex1_list) - 1 == index:
                        break
                  sum_each_num += int(num)
            if sum_each_num % 3 != 0:
                  print(-1)
            else:

                  print("".join(ex1_list))










Solution("30")
print("==========================================")
Solution("102")
print("==========================================")
Solution("2931")
print("==========================================")
Solution("88755420")
print("==========================================")
