from operator import le
import re


print("a is better than b")

#if 문
a = 1
b = 2
if a < b :
    print("a는 b보다 작다")
    
# 반복문 for
for a in [1,2,3]:
    print(a)
    
# 반복문 while
print("while 문 사용")
i = 0
while i < 3:
    i = i + 1
    print(i)

print("add 함수 결과 ")
# 파이썬 함수
def add(a,b):
    return a+b

add(3,5)


# 문자열 안에 작은따옴표 포함시키기
food = "Python's favorite food is perl"
print(food)

# 여러 줄인 문자열 변수에 대입하기
text = "Life is too short\n파이썬 공부"
text2 = """
첫 번째 줄
두 번째 줄
"""

print(text)
print(text2)

# 문자열 연산 
# 1. 문자열 더해서 연결하기 (Concatenation)
head = "Python"
tail = " 공부중"
head + tail

# 2. 문자열 곱하기
a = '곱하기'
a * 3

# 3. 문자열 곱셈 예제
print("=" * 10 )
print('열공하자')
print("=" * 10 )

# 4. 문자열 길이 구하기 len 함수 사용
name = '김재윤'
name2 = 'Alex'

len(name)
len(name2)

if len(name) == 3:
    print("김재윤입니다.")
else:
    print("알렉스입니다")

# 문자열 인덱싱, 뒤에서부터 카운트하려면 숫자 앞에 -를 추가
# 앞에서부터 카운트 할 떄는 0부터 시작이지만 뒤에서부터 카운트할떄는 1부터이다. 
a = '파이썬 공부중입니다.'
a[2]
a[-2]
a[0:-2]
a[0:9]

# 슬라이싱으로 문자열 나누기
a = "20220915Rainy"
date = a[:8]
weather = a[8:]

date
weather

# Pithon 문자열을 Python으로 바꾸려면
# 문자열 자료형은 요솟값을 변경할 수 없다. 
a = 'Pithon'
a[1]
a[1] = 'y'
a

#  슬라이싱기법을 사용해서 바꿔준다. 
a = 'Pithon'
a[:1]
a[2:]
a[:1] + 'y' + a[2:]
