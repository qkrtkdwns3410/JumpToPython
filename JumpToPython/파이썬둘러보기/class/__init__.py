"""
 *packageName    : 
 * fileName       : __init__.py
 * author         : ipeac
 * date           : 2022-03-15
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-03-15        ipeac       최초 생성
 """


class Calculator:

    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result


cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))
