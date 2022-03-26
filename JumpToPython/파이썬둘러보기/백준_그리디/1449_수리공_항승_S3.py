"""
 *packageName    : 
 * fileName       : 1449_수리공_항승
 * author         : qkrtk
 * date           : 2022-03-25
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-03-25        qkrtk       최초 생성
 """


def Solution(n, l, tape_list):
      tape_list.sort()
      max_tape_x = 0
      cnt = 0
      for index, num in enumerate(tape_list):
            if num > max_tape_x:
                  cnt += 1
                  max_tape_x = num + l - 1
      
      print(cnt)


n, l = map(int, input().split())
tape_list = list(map(int, input().split()))
Solution(n, l, tape_list)

# Solution(4, 2, [1, 2, 100, 101])
# Solution(4, 3, [1, 2, 3, 4])
# Solution(3, 1, [3, 2, 1])
