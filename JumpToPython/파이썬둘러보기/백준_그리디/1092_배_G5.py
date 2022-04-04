"""
 *packageName    : 
 * fileName       : 1092_배_G5
 * author         : qkrtk
 * date           : 2022-04-04
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-04-04        qkrtk       최초 생성
 """


def Solution(n, crain_weight_limit_list, box_num, box_weight_list):
      print("==========================================")
      print("n : %s " % n)
      able_list = [0 for _ in range(n)]
      print("able_list : %s " % able_list)
      crain_weight_limit_list.sort(reverse=True)
      
      print("crain_weight_limit_list : %s " % crain_weight_limit_list)
      print("box_num : %s " % box_num)
      
      box_weight_list.sort(reverse=True)
      print("box_weight_list : %s " % box_weight_list)
      result = 0
      # 모든 박스를 배로 옮길 수 없는 경우
      if max(crain_weight_limit_list) < max(box_weight_list):
            print(-1)
            return
      
      # 배로 옮길 수 있는 경우
      while box_weight_list:
            if not box_weight_list:
                  break
            for crane in crain_weight_limit_list:
                  for box in box_weight_list:
                        if crane >= box:
                              box_weight_list.remove(box)
                              break
            result += 1
      print(result)









Solution(3, [6, 8, 9], 5, [2, 5, 2, 4, 7])
Solution(2, [19, 20], 7, [14, 12, 16, 19, 16, 1, 5])
Solution(4, [23, 32, 25, 28], 10, [5, 27, 10, 16, 24, 20, 2, 32, 18, 7])
Solution(10, [11, 17, 5, 2, 20, 7, 5, 5, 20, 7], 10, [5, 27, 10, 16, 24, 20, 2, 32, 18, 7])

n = int(input())
crain_weight_limit_list = list(map(int, input().split()))
box_num = int(input())
box_weight_list = list(map(int, input().split()))
Solution(n, crain_weight_limit_list, box_num, box_weight_list)
