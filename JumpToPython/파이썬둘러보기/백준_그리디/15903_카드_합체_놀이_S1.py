"""
 *packageName    : 
 * fileName       : 15903_카드_합체_놀이_S1
 * author         : qkrtk
 * date           : 2022-03-19
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-03-19        qkrtk       최초 생성
 """
import sys


def Solution(card_count, card_sum_count, card_status_list):
      sum_of_it = 0
      cnt = 0

      for _ in range(card_sum_count):

            sum_of_it = card_status_list[0] + card_status_list[1]

            card_status_list[0] = sum_of_it
            card_status_list[1] = sum_of_it
            card_status_list.sort()
            cnt += 1

      print(sum(card_status_list))



n, m = map(int, sys.stdin.readline().split())
card_list = list(map(int, sys.stdin.readline().split()))
card_list.sort()
Solution(n, m, card_list)
