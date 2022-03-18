"""
 *packageName    : 
 * fileName       : 1541_잃어버린_괄호_S2
 * author         : ipeac
 * date           : 2022-03-17
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-03-17        ipeac       최초 생성
 """


def Solution(susik):
      susik_list = list(susik.split("-"))
      result = 0
      susik_plus = []
      for index, num_str in enumerate(susik_list):
            if '+' in num_str:
                  temp_list = map(int, num_str.split("+"))
                  temp_sum = sum(temp_list)
                  susik_list[index] = str(temp_sum)

      for index, num in enumerate(susik_list):
            if index == 0:
                  result += int(num)
            else:
                  result -= int(num)
      print(result)


a = input()
Solution(a)

Solution("55-50+4+100-200+55")
print("==========================================")
Solution("55-50+40")
print("==========================================")
Solution("10+20+30+40")
print("==========================================")
Solution("00009-00009")
