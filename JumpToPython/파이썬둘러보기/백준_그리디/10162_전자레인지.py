"""
 *packageName    : 
 * fileName       : 6001_출력하기01
 * author         : ipeac
 * date           : 2022-03-16
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-03-16        ipeac       최초 생성
 """
"""
A - 5분 B - 1분 C - 10초
T-  초단위

"""
a = 300
b = 60
c = 10

t = int(input())

counta = 0
countb = 0
countc = 0

while (t >= 300):
    counta += 1
    t -= a

while (t >= 60):
    countb += 1
    t -= b

while t > 0:
    countc += 1
    t -= c

if counta == 0 and countb == 0 and countc == 0 or t != 0:
    print(-1)

else:
    print(counta, countb, countc)
