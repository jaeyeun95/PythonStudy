# 내장 함수
# abs -> abs(x) x의 절댓값을 돌려주는 함수
abs(-1)
# all -> all(x) x가 참이면 True, 거짓이 하나라도 있으면 False를 리턴한다.
all([1,2,3])
all([1,2,3,0])
# any <-> all, x가 하나라도 참이 있으면 True, 모두 거짓일 경우에만 False
any([1,2,3,0])
any([0, ""])
# chr -> 아스키코드값을 입력받아 해당하는 문자를 출력한다.
chr(97)
# dir -> 객체가 자체적으로 가지고 있는 변수나 함수를 보여 준다. 
dir([1,2,3])
dir({'1':'1'})
# divmod -> divmod(a,b) = a 를 b로 나눈 몫과 나머지를 튜플 형태로 돌려주는 함수이다.
divmod(7, 3)
# enumerate -> 순서가 있는 자료형을 입력으로 받아 인덱스 값을 포함하는 enumerate 객체를 돌려준다.
for i, name in enumerate(['body', 'foo', 'bar']):
    print(i, name)
# eval -> eval(expression)은 실행 가능한 문자열을 입력으로 받아 문자열을 실행한 결괏값을 돌려주는 함수
# 보통 입력받은 문자열로 파이썬 함수나 클래스를 동적으로 실행하고 싶을 때 사용한다.
eval('1+2')
eval("'hi' + 'a'")
# filter
# filter 함수는 첫 번째 인수로 함수 이름을, 두 번째 인수로 그 함수에 차례로 들어갈 반복 가능한 자료형을 받는다. 
# 그리고 두 번째 인수인 반복 가능한 자료형 요소가 첫 번째 인수인 함수에 입력되었을 때 반환 값이 참인 것만 묶어서 돌려준다.
def positive(l):
    result = [] # 반환 값이 참인 것만 걸러내서 저장할 변수
    for i in l:
        if i > 0:
            # print(i)
            result.append(i)
        return result

print(positive([1, -3, 2, 0, -5, 6]))
positive([1, -3, 2, 0, -5, 6])

def positive2(x):
    return x > 0

print(list(filter(positive, [1, -3, 2, 0, -5, 6])))

# hex -> hex(x) 는 정수값을 입력받아 16진수로 변환하여 돌려주는 함수이다.
hex(234)
# id -> id(obejct)는 객체를 입력받아 객체의 고유 주소 값을 돌려주는 함수이다.
a = 3
id(3)
id(a)

# input -> input([prompt]) 매개변수로 문자열을 주면 다음 세 번째 예에서 볼 수 있듯이 그 문자열은 프롬프트가 된다.
a = input()
a
b = input('Enter : ') # -> 자바에서 스캐너
b
# int -> int(x) 정수를 입력으로 받으면 그대로 돌려준다.
int('3')