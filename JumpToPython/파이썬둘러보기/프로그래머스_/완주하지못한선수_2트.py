"""
 *packageName    : 
 * fileName       : 완주하지못한선수_2트
 * author         : jihye94
 * date           : 2022-06-05
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-06-05        jihye94       최초 생성
 """
from collections import Counter

def solution(participant, completion):
      participant.sort()
      completion.sort()
      answer = Counter(participant) - Counter(completion)
      
      return list(answer.keys())[0]

solution(["leo", "kiki", "eden"], ["eden", "kiki"])
print("==========================================")
solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"])
print("==========================================")
solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"])
print("==========================================")
