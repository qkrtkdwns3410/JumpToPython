"""
 *packageName    : 
 * fileName       : 해시_완주하지못한선수
 * author         : ipeac
 * date           : 2022-04-20
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-04-20        ipeac       최초 생성
 """
import collections


def solution(participant, completion):
      participant.sort()
      completion.sort()
      res = collections.Counter(participant) - collections.Counter(completion)
      return list(res.keys())[0]



solution(["leo", "kiki", "eden"], ["eden", "kiki"])
solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"])
solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"])
