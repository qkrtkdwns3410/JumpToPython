"""
 *packageName    : 
 * fileName       : 4796_캠핑_S5
 * author         : qkrtk
 * date           : 2022-03-17
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-03-17        qkrtk       최초 생성
 """

"""
연속하는 P 일중 , L일 동안만 사용할 수 있습니다.
이제 V일 짜리 휴가를 시작함

캠핑장 최대 며칠동안 사용가능한가??
"""
case_count = 1
check_correct = True



def Solution(l, p, v):
      global case_count
      global check_correct
      seq_date_able = l
      seq_date = p
      vacation_date = v

      if seq_date_able == 0 and seq_date == 0 and vacation_date == 0:
            check_correct = False
            return

      able_value = vacation_date // seq_date
      print("able_value : %s " % able_value)

      result_value1 = able_value * seq_date_able
      print("result_value1 : %s " % result_value1)

      result_value2 = vacation_date - (seq_date * able_value)
      print("result_value2 : %s " % result_value2)

      if result_value2 > seq_date_able:
            result_value2 = seq_date_able
            print("result_value2 : %s " % result_value2)
      else:
            pass

      result = result_value1 + result_value2

      print("Case %d: %d" % (case_count, result))
      case_count += 1





while check_correct:
      l, p, v = map(int, input().split())
      Solution(l, p, v)


# L P V
# Solution("5 8 20")
# print("==========================================")
# Solution("5 8 17")
# print("==========================================")
# Solution("0 0 0")
