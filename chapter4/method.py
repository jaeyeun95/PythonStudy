# 4. 함수
def add(a,b):   # a,b 는 매개변수
    return a + b
a = 3
b = 4
c = add(a,b)
print(c)

# 함수의 형태
# 1. 일반적인 함수
def add(a,b):
    result = a + b
    return result
a = add(3,4)
print(a)
# 2. 입력값이 없는 함수
def say():
    return 'Hi'
a = say()
print(a)
# 3. 결괏값이 없는 함수
def add(a, b):
    print('%d, %d의 합은 %d입니다.' % (a, b, a+b) )
a = add(3,4)
print(a)
# 입력값도 결괏괎도 없는 함수
def say():
    print('Hi')
say()

# 매개변수 지정하여 호출하기
def add(a, b):
    return a+b
result = add(a=3, b=7)
print(result)
# 입력값이 몇 개가 될지 모르는 상황에서 함수 만들기
def add_many(*args):
    result = 0
    for i in args:
        result = result + i
    return result
result = add_many(1,2,3)
print(result)
# 매개변수로 *args 외에 다른 것도 사용 가능하다.
def add_mul(choice, *args):
    if choice == 'add':
        result = 0
        for i in args:
            result = result +i
    elif choice == 'mul':
        result = 1
        for i in args:
            result = result * i
    return result
result = add_mul('mul', 1,2,3,4,5)
print(result)