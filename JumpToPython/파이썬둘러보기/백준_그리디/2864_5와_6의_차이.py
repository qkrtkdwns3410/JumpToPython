"""
 *packageName    : 
 * fileName       : 2864_5와_6의_차이
 * author         : ipeac
 * date           : 2022-03-16
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-03-16        ipeac       최초 생성
 """


def solution(ex1):
      a, b = map(str, ex1.strip().split())

      a_list = list(a)
      print("a_list : %s " % a_list)
      b_list = list(b)
      print("b_list : %s " % b_list)
      if '5' in a_list:
            for index, num in enumerate(a_list):
                  if num == '5':
                        a_list[index] = '6'
      if '5' in b_list:
            for index, num in enumerate(b_list):
                  if num == '5':
                        b_list[index] = '6'
      maxValue = int("".join(map(str, a_list))) + int("".join(map(str, b_list)))
      print("maxValue : %s " % maxValue)
      print("==========================================")

      if '6' in a_list:
            for index, num in enumerate(a_list):
                  if num == '6':
                        a_list[index] = '5'
      if '6' in b_list:
            for index, num in enumerate(b_list):
                  if num == '6':
                        b_list[index] = '5'
      minValue = int("".join(map(str, a_list))) + int("".join(map(str, b_list)))
      print("minValue : %s " % minValue)
      print(minValue, maxValue)








print("==========================================")
solution("11 25")
print("==========================================")
solution("1430 4862")
print("==========================================")
solution("16796 58786")
print("==========================================")
