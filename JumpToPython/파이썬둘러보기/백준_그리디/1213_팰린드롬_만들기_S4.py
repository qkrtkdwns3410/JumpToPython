"""
 *packageName    : 
 * fileName       : 1213_팰린드롬_만들기_S4
 * author         : qkrtk
 * date           : 2022-03-30
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-03-30        qkrtk       최초 생성
 """
from collections import Counter


def Solution(letters):
      global odd_alpha, odd_alpha_value
      print("==========================================")
      letters = list(letters)
      letters.sort()
      temp_str_list = []
      
      # 홀수 개수가 2개 이상이면 팰린드롬이 성립하지 않는다.
      check_odd_count = Counter(letters)
      print("check_odd_count : %s " % check_odd_count)
      
      print("letters : %s " % letters)
      center = ""
      for alpha, value in check_odd_count.items():
            print("alpha : %s " % alpha)
            print("value : %s " % value)
            
            if value % 2 != 0:
                  # 해당 센터 값이 존재한다면 홀수가 2개라는 반증이기에 .. 팰린드롬이 성립할 수 없습니다.
                  if center:
                        print("I'm Sorry Hansoo")
                        return
                  center = alpha
                  for _ in range(value // 2):
                        temp_str_list.append(alpha)
            else:
                  for _ in range(value // 2):
                        temp_str_list.append(alpha)
      temp_str_list.sort()
      print("temp_str_list : %s " % temp_str_list)
      print(''.join(temp_str_list) + center + ''.join(temp_str_list[::-1]))





input_str = input()
Solution(input_str)

Solution("AABB")
Solution("ABABA")
Solution("ABACABA")
Solution("ABCD")
