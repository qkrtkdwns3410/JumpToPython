"""
 *packageName    : 
 * fileName       : 11497_통나무_건너뛰기_S1
 * author         : qkrtk
 * date           : 2022-03-19
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-03-19        qkrtk       최초 생성
 """
import sys


def Solution(wood_count, wood_height_list):
      print("wood_count : %s " % wood_count)
      print("wood_height_list : %s " % wood_height_list)
      wood_height_copy_list = []
      wood_height_diff = []
      if len(wood_height_list) % 2 == 0:
            wood_height_copy_list.extend(wood_height_list[0::2])
            wood_height_copy_list.extend(wood_height_list[-1::-2])

      else:
            wood_height_copy_list.extend(wood_height_list[0::2])
            wood_height_copy_list.extend(wood_height_list[-2::-2])

      print("wood_height_copy_list : %s " % wood_height_copy_list)

      for index, num in enumerate(wood_height_copy_list):
            if index == len(wood_height_copy_list) - 1:
                  wood_height_diff.append(abs(wood_height_copy_list[index] - wood_height_copy_list[0]))
            else:
                  wood_height_diff.append(abs(wood_height_copy_list[index] - wood_height_copy_list[index + 1]))

      wood_height_diff.sort(reverse=True)
      print(wood_height_diff[0])




T = int(sys.stdin.readline())

for _ in range(T):
      N = int(sys.stdin.readline())
      wood_height_list = list(map(int, sys.stdin.readline().split()))
      wood_height_list.sort()
      Solution(N, wood_height_list)
