"""
 *packageName    : 
 * fileName       : 1931_회의실_배정_S2
 * author         : ipeac
 * date           : 2022-03-17
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-03-17        ipeac       최초 생성
 """


def Solution(room_list):
      last = 0
      cnt = 0

      for i, j in room_list:
            if i >= last:
                  last = j
                  cnt += 1

      print(cnt)





N = int(input())
room_list = []
for _ in range(N):
      first, second = map(int, input().split())
      room_list.append([first, second])
room_list = sorted(room_list, key=lambda start: start[0])
room_list = sorted(room_list, key=lambda end: end[1])

Solution(room_list)
