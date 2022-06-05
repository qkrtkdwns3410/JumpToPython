"""
 *packageName    : 
 * fileName       : 위장
 * author         : jihye94
 * date           : 2022-06-05
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-06-05        jihye94       최초 생성
 """
from collections import Counter
from functools import reduce

def solution(clothes):
      print("clothes : %s " % clothes)
      
      # 1. 의상 종류별 Counter를 만든다.
      counter = Counter([type for clothe, type in clothes])
      print("counter : %s " % counter)
      
      # 2. 모든 종류의 count +1 누적.. 곱...
      answer = reduce(lambda acc, cur: acc * (cur + 1), counter.values(), 1) - 1
      
      return answer


solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban",
                                                                     "headgear"]])
print("==========================================")
solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]])
