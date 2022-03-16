"""
 *packageName    : 
 * fileName       : CalFour
 * author         : ipeac
 * date           : 2022-03-16
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-03-16        ipeac       최초 생성
 """
import mod1


class FourCal:

    def __init__(self, second, first):
        self.first = first
        self.second = second

    def setdata(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result

    def div(self):
        result = self.first / self.second
        return result


class MoreFourCal(FourCal):

    def pow(self):
        result = self.first ** self.second
        return result


class SafeFourCal(FourCal):

    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second


a = SafeFourCal(4, 0)

b = add(4, 2)

print(a.div())
print(b)
