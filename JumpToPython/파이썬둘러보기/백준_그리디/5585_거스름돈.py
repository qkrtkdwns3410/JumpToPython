"""
 *packageName    : 
 * fileName       : 5585_거스름돈
 * author         : ipeac
 * date           : 2022-03-16
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-03-16        ipeac       최초 생성
 """


def Solution(payMoney):
      my_budget = 1000
      count_500 = 0
      count_100 = 0
      count_50 = 0
      count_10 = 0
      count_5 = 0
      count_1 = 0

      print("payMoney : %s " % payMoney)
      my_budget -= int(payMoney)
      
      while my_budget >= 500:
            my_budget -= 500
            count_500 += 1
      while my_budget >= 100:
            my_budget -= 100
            count_100 += 1
      while my_budget >= 50:
            my_budget -= 50
            count_50 += 1
      while my_budget >= 10:
            my_budget -= 10
            count_10 += 1
      while my_budget >= 5:
            my_budget -= 5
            count_5 += 1
      while my_budget >= 1:
            my_budget -= 1
            count_1 += 1

      print(count_500 + count_100 + count_50 + count_10 + count_5 + count_1)







Solution("380")
print("==========================================")
Solution("1")
print("==========================================")
