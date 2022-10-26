class FourCal():
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result

a = FourCal(4, 2)
print(a.first)
a.add()
a.div()
a.mul()

# 클래스의 상속 
# a의 b제곱을 계산하는 기능 추가 pow
class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result

b = MoreFourCal(4,2)
b.add()
b.mul()
b.pow()
c = FourCal(4,0)
c.div()
# 메소드 오버라이딩
class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second
c = SafeFourCal(4,0)
c.div()
# p204 나혼자 코딩 풀기