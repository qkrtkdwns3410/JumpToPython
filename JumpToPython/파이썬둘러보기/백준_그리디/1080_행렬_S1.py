"""
 *packageName    : 
 * fileName       : 1080_행렬_S!
 * author         : qkrtk
 * date           : 2022-03-18
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-03-18        qkrtk       최초 생성
 """


def Solution(arr_two_list_init, arr_two_list_object):
      count = 0
      print("arr_two_list_init : %s " % arr_two_list_init)
      print("arr_two_list_object : %s " % arr_two_list_object)

      for i in range(N - 2):
            for j in range(M - 2):
                  if arr_two_list_init[i][j] != arr_two_list_object[i][j]:
                        reverse(i, j)
                        count += 1
      if check():
            print(count)
      else:
            print("-1")


def reverse(x, y):
      for i in range(x, x + 3):
            for j in range(y, y + 3):
                  arr_two_list_init[i][j] = 1 - arr_two_list_init[i][j]


def check():
      for i in range(N):
            for j in range(M):
                  if arr_two_list_init[i][j] != arr_two_list_object[i][j]:
                        return False

      return True






N, M = map(int, input().split())
arr_two_list_object = []
arr_two_list_init = [list(map(int, list(input()))) for _ in range(N)]

for _ in range(N):
      a = map(int, input().split())
      arr_two_list_object.append(a)

Solution(arr_two_list_init, arr_two_list_object)
