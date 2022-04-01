"""
 *packageName    : 
 * fileName       : 2847_게임을_만든_동준이_S4
 * author         : qkrtk
 * date           : 2022-04-01
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-04-01        qkrtk       최초 생성
 """


def Solution(n, level_list):
      print("==========================================")
      print("n : %s " % n)
      print("level_list : %s " % level_list)
      
      cnt = 0
      
      level_list.reverse()
      print("level_list : %s " % level_list)
      answer = 0
      
      for index in range(len(level_list) - 1):
            print("index : %s " % index)
            
            if level_list[index] <= level_list[index + 1]:
                  diff = level_list[index + 1] - level_list[index] + 1
                  answer += diff
                  level_list[index + 1] -= diff
                  print("level_list : %s " % level_list)
      print(answer)



Solution(3, [5, 5, 5])
Solution(3, [1, 10, 3])
Solution(2, [3, 2])
Solution(4, [5, 3, 7, 5])

n = int(input())

list_list = []
for _ in range(n):
      list_list.extend(input().split())
list_list = list(map(int, list_list))

Solution(n, list_list)
