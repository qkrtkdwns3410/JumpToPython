"""
 *packageName    : 
 * fileName       : 1080_행렬_S!
 * author         : qkrtk
 * date           : 2022-03-18
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-03-18        qkrtk       최초 생성
 """


def Solution(arr_two_list_init, arr_two_list_object):
      print("arr_two_list_init : %s " % arr_two_list_init)
      print("arr_two_list_object : %s " % arr_two_list_object)
      









N, M = map(int, input().split())
arr_two_list_init = []
arr_two_list_object = []

for _ in range(N):
      a = input()
      arr_two_list_init.append(a)

for _ in range(N):
      a = input()
      arr_two_list_object.append(a)

Solution(arr_two_list_init, arr_two_list_object)
