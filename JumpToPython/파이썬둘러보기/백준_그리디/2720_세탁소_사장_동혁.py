"""
 *packageName    : 
 * fileName       : 2720_세탁소_사장_동혁
 * author         : ipeac
 * date           : 2022-03-16
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-03-16        ipeac       최초 생성
 """
"""
 
 """
test_case = int(input())
a = range(0, test_case)

for i in a:
    case = int(input())
    countQ = 0
    countD = 0
    countN = 0
    countP = 0

    while case >= 25:
        countQ += 1
        case -= 25
    while case >= 10:
        countD += 1
        case -= 10
    while case >= 5:
        countN += 1
        case -= 5
    while case >= 1:
        countP += 1
        case -= 1

    print(countQ, countD, countN, countP)
