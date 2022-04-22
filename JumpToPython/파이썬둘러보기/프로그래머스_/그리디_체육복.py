"""
 *packageName    : 
 * fileName       : 그리디_체육복
 * author         : ipeac
 * date           : 2022-04-21
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-04-21        ipeac       최초 생성
 """


def solution(n, lost, reserve):
      print("==========================================")
      print("n : %s " % n)
      print("lost : %s " % lost)
      print("reserve : %s " % reserve)
      
      lost.sort()
      set_list1 = set(lost)
      set_list2 = set(reserve)
      lost = list(set_list1 - set_list2)
      reserve = list(set_list2 - set_list1)
      answer = n - len(lost)
      
      for i in range(len(lost)):
            if lost[i] - 1 in reserve:
                  reserve.remove(lost[i] - 1)
                  answer += 1
            
            elif lost[i] in reserve:
                  reserve.remove(lost[i])
                  answer += 1
            
            elif lost[i] + 1 in reserve:
                  reserve.remove(lost[i] + 1)
                  answer += 1
            
            print("reserve : %s " % reserve)
            print("answer : %s " % answer)
      
      return answer



solution(5, [2, 4], [1, 3, 5])
solution(5, [2, 4], [3])
solution(3, [3], [1])
solution(3, [1, 2], [2, 3])
