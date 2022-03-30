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
      print("==========================================")
      letters = list(letters)
      letters.sort()
      
      # 홀수 개수가 2개 이상이면 팰린드롬이 성립하지 않는다.
      check_odd_count = Counter(letters)
      print("check_odd_count : %s " % check_odd_count)
      
      print("letters : %s " % letters)
      odd_num_count = 0
      
      for num, alpha in enumerate(check_odd_count):
            if num % 2 != 0:
                  odd_num_count += 1
            if odd_num_count >= 2:
                  print("I'm Sorry Hansoo")
                  return
      # 체크완료
      
      #
      
      name_dic = {}



Solution("AABB")
Solution("ABABA")
Solution("ABACABA")
Solution("ABCD")
