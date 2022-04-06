"""
 *packageName    : 
 * fileName       : lotto_level1
 * author         : ipeac
 * date           : 2022-04-04
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-04-04        ipeac       최초 생성
 """


def solution(lottos, win_nums):
      print("==========================================")
      print("lottos : %s " % lottos)
      print("win_nums : %s " % win_nums)
      min_cnt = 0
      max_cnt = 0
      for index, num in enumerate(lottos):
            if lottos[index] in win_nums and lottos[index] != 0:
                  win_nums.remove(lottos[index])
                  min_cnt += 1
                  max_cnt += 1
            elif lottos[index] == 0:
                  max_cnt += 1
      print("max_cnt : %s " % max_cnt)
      print("min_cnt : %s " % min_cnt)
      answer = []
      
      rank(max_cnt, answer)
      rank(min_cnt, answer)
      print("answer : %s " % answer)
      
      return answer


def rank(correct, answer):
      if correct == 6:
            answer.append(1)
      elif correct == 5:
            answer.append(2)
      elif correct == 4:
            answer.append(3)
      elif correct == 3:
            answer.append(4)
      elif correct == 2:
            answer.append(5)
      else:
            answer.append(6)
      return


solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19])
solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25])
solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35])
