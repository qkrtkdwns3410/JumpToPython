"""
 *packageName    : 
 * fileName       : 11034_캥거루_세마리2
 * author         : ipeac
 * date           : 2022-03-16
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-03-16        ipeac       최초 생성
 """
import sys

while True:
    try:
        a, b, c = map(int, sys.stdin.readline().split())

        if (abs(a - b) >= abs(b - c)):
            if (abs(a - b) == 0):
                print(0)

            print(abs(a - b) - 1)
        else:
            if (abs(b - c) == 0):
                print(0)
            print(abs(b - c) - 1)

    except:
        break
