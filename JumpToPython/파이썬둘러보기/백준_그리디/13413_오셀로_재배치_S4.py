"""
 *packageName    : 
 * fileName       : 13413_오셀로_재배치_S4
 * author         : qkrtk
 * date           : 2022-03-17
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-03-17        qkrtk       최초 생성
 """
arr = []


def Solution(n, init_place_para, object_place_para):
      for num in range(len(init_place_para)):
            if init_place_para[num] != object_place_para[num]:
                  arr.append(init_place_para[num])

      if arr.count('W') >= arr.count('B'):
            print(arr.count('W'))
      else:
            print(arr.count('B'))

      return


T = int(input())
for repeat in range(0, T):
      N = int(input())
      init_place = input()
      object_place = input()

      Solution(N, init_place, object_place)
      arr = []
