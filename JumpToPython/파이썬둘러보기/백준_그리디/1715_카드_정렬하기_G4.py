"""
 *packageName    : 
 * fileName       : 1715_카드_정렬하기
 * author         : qkrtk
 * date           : 2022-03-21
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-03-21        qkrtk       최초 생성
 """
import heapq
import sys

n = int(sys.stdin.readline())
cards = []
for _ in range(n):
      heapq.heappush(cards, int(sys.stdin.readline()))

print("heapq : %s " % heapq)

if len(cards) == 1:
      print(0)
else:
      result = 0
      while len(cards) > 1:
            print("==========================================")
            print("cards : %s " % cards)
            
            min_value = heapq.heappop(cards)
            print("min_value : %s " % min_value)
            
            min_value_next = heapq.heappop(cards)
            print("min_value_next : %s " % min_value_next)
            
            result += min_value + min_value_next
            print("result : %s " % result)
            heapq.heappush(cards, min_value + min_value_next)
            print("cards : %s " % cards)
      print(result)









# Solution(3, [10, 20, 40])
# 100
# Solution(5, [10, 20, 40, 30, 20])
# #
