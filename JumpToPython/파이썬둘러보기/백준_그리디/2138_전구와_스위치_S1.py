"""
 *packageName    : 
 * fileName       : 2138_전구와_스위치_S1
 * author         : ipeac
 * date           : 2022-03-19
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-03-19        ipeac       최초 생성
 """
import sys


N = int(sys.stdin.readline())
init_list = list(map(int, input()))
object_list = list(map(int, input()))


def change(num):
      if num == 0:
            num = 1

      else:
            num = 0

      return num


def switch(init_list, count):
      global N
      if count == 1:
            init_list[0] = change(init_list[0])
            init_list[1] = change(init_list[1])

      for i in range(1, N):
            if init_list[i - 1] != object_list[i - 1]:
                  count += 1
                  init_list[i - 1] = change(init_list[i - 1])
                  init_list[i] = change(init_list[i])
                  if i != N - 1:
                        init_list[i + 1] = change(init_list[i + 1])
      if init_list == object_list:
            return count

      else:
            return -1







res1 = switch(init_list[:], 0)
res2 = switch(init_list[:], 1)

if res1 >= 0 and res2 >= 0:
      print(min(res1, res2))

elif res1 >= 0 and res2 < 0:
      print(res1)

elif res1 < 0 and res2 >= 0:
      print(res2)

else:
      print(-1)
