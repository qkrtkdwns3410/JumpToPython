"""
 *packageName    : 
 * fileName       : 1946_신입_사원_S1
 * author         : ipeac
 * date           : 2022-03-17
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-03-17        ipeac       최초 생성
 """
import sys


def Solution(each_rank):
      cnt = 1

      global N

      each_rank.sort()
      max_value = each_rank[0][1]

      for i in range(1, N):
            if max_value > each_rank[i][1]:
                  cnt += 1
                  max_value = each_rank[i][1]

      print(cnt)










N = 0
T = int(input())
each_person_rank = []
for _ in range(T):
      N = int(sys.stdin.readline())
      for _ in range(N):
            paper_rank, interview_rank = map(int, sys.stdin.readline().split())
            each_person_rank.append([paper_rank, interview_rank])

      Solution(each_person_rank)
      each_person_rank = []
