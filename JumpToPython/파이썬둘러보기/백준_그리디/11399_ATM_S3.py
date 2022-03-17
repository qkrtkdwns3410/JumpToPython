"""
 *packageName    : 
 * fileName       : 11399_ATM_S3
 * author         : qkrtk
 * date           : 2022-03-17
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-03-17        qkrtk       최초 생성
 """


def Solution(peple_time_list):
      peple_time_list = map(int, peple_time_list)
      peple_time_list = sorted(peple_time_list)

      print("peple_time_list : %s " % peple_time_list)
      result_sum = 0
      result = 0
      for num in peple_time_list:
            result_sum += num
            result += result_sum
      print(result)









N = 5
para_list = list("3 1 4 3 2".split())
Solution(para_list)
