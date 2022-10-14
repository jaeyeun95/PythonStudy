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

# 키워드 파라미터
# 키워드 파라미터를 사용할 때는 매개변수 앞에 별 두개(**)를 붙여서 사용한다.
def print_kwargs(**kwargs):
    print(kwargs)
print_kwargs(a=1)
print_kwargs(name='foo', age=3)

# 함수의 결과값은 언제나 하나이다.
def add_and_mul(a,b):
    return a+b, a*b
result = add_and_mul(3,4)
result
# 리턴 값을 2개의 결괏값으로 받으려면 변수를 2개 선언해줘야 한다.
result1, result2 = add_and_mul(3,4)
result1
result2
# 특별한 상황일 때 함수를 빠져나가고 싶다면 return을 단독으로 써서 함수를 즉시 빠져나갈 수 있다. 
def say_nic(nick):
    if nick == '바보':
        return
    print('나의 별명은 %s입니다.' % nick)
say_nic('야호')
# 매개변수에 초깃값 미리 설정하기
def say_myself(name, old, man=True):
    print('나의 이름은 %s입니다.' % name)
    print('나이는 %d살입니다.' % old)
    if man:
        print('남자입니다.')
    else:
        print('여자입니다.')
say_myself('박응용', 27)
say_myself('박응용', 28, True)

# 함수 안에서 함수 밖의 변수를 변경하는 방법
# 1. return 사용하기
a = 1
def vartest(a):
    a = a + 1
    return a

a = vartest(a)
print(a)
# 2. global 명령어 사용하기
a = 1
def vartest():
    global a
    a = a + 1

vartest()
print(a)
# lambda
# 함수를 생성할 때 사용하는 예약어로 def와 동일한 역할을 한다.
# lambda 매개변수1, 매개변수2 ... : 매개변수를 사용한 표현식
# lambda 식
add = lambda a, b: a + b
result = add(3, 4)
print('lambda 결과 %d '% result)
# def 식
def add(a, b):
    return a + b
result = add(4,5)
print('def사용식 결과 %d '% result)
