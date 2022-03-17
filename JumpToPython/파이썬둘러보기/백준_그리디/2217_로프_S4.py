"""
 *packageName    : 
 * fileName       : 2217_로프_S4
 * author         : qkrtk
 * date           : 2022-03-17
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-03-17        qkrtk       최초 생성
 """


def Solution(max_list):
      global N
      max_value = []
      while True:
            if len(max_list) == 0:

                  break
            max_value.append(max_list[0] * int(len(max_list)))
            max_list.remove(max_list[0])
      max_value.sort(reverse=True)
      print("max_value : %s " % max_value)
      print(max_value[0])









N = int(input())
can_max_weight = []
for repeat in range(0, N):
      can_max_weight.append(int(input()))
can_max_weight.sort()
Solution(can_max_weight)
