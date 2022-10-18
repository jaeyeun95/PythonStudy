# 파이썬 코드로 계산기
# 계산기가 1개일 경우
result = 0

def add(num):
    global result
    result += num
    return result

print(add(3))
print(add(5))

# 계산기가 2개 필요한 경우 각각 계산기의 결과값을 유지해야 함으로 함수를 2개로 나누어야 한다. 
result1 = 0
result2 = 0

def add1(num):
    global result1
    result1 += num
    return result1

def add2(num):
    global result2
    result2 += num
    return result2

print(add1(3))
print(add1(4))
print(add2(5))
print(add2(10))

# 해당 경우를 클래스를 사용해서 할 경우
class Calculator:
    def __init__(self):
        self.result = 0
        
    def add(self, num):
        self.result += num
        return self.result
    
    def sub(self, num):
        self.result -= num
        return self.result

cal1 = Calculator()
cal2 = Calculator()
print(cal1.add(4))
print(cal1.add(2))
print(cal2.add(4))
print(cal2.add(5))