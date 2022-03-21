"""
 *packageName    : 
 * fileName       : 1026_보물_S4
 * author         : qkrtk
 * date           : 2022-03-21
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-03-21        qkrtk       최초 생성
 """
import copy


def Solution(length, a_list, b_llist):
      print("==========================================")
      print("length : %s " % length)
      print("a_list : %s " % a_list)
      print("b_llist : %s " % b_llist)
      a_list = sorted(a_list)
      print("a_list : %s " % a_list)
      
      b_llist_copy = copy.deepcopy(b_llist)
      b_llist_copy.sort(reverse=True)
      print("b_llist_copy : %s " % b_llist_copy)
      sum = 0
      index = 0
      while length:
            sum += a_list[index] * b_llist_copy[index]
            index += 1
            length -= 1
      print(sum)



a = int(input())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

Solution(a, a_list, b_list)
