# 문자열 포맷팅
# 1. 숫자 바로 대입 -> %d
'I eat %d apples.' % 3

# 2. 문자열 바로 대입 -> %s
'I eat %s apples.' % 'five'

# 3. 숫자 값을 나타내는 변수로 대임 -> d나 s 둘다 되네..
number = 3
'I eat %s apples.' % number

# 4. 2개 이상의 값 넣기  -> 마지막 % 다음 괄호 안에 콤마로 구분하여 각각의 값을 넣어주면 된다. 
number = 10
day = 'three'
'I ate %d apples. so I was sick for %s days' % (number, day)

#  포맷 코와 숫자 함께 사ㅇㅏ기
#  1. 정렬과 공백 -> hi가 오른쪽 정렬됨
"%10s" % "hi"
# 왼쪽 정렬
"%-10s" % "hi"
# 2. 소수점 표현하기 -> 0.4 = 소수점 네 번째 자리까지만 나타내고 싶은 경우 사용
"%0.4f" % 3.42133234

# format 함수를 사용한 포매팅
# 1. 숫자 바로 대입하기
"I eat {0} apples".format(3)
# 2. 문자열 바로 대입하기 
"I eat {0} apples".format("five")
# 3. 숫자 값을 가진 변수로 대입하기
number = 3
"I eat {0} apples".format(number)
# 4. 2개 이상의 값 넣기
number = 10
day = "three"
"I ate {0} apples. so I was sic for {1} days".format(number, day)
# 5. 이름으로 넣기
"I eat {number} apples. so I was sic for {day} days".format(number=10, day="three")
# 6. 인덱스와 이름을 혼용해서 넣기
"I eat {0} apples. so I was sic for {day} days".format(10, day = 3)
# 7. 왼쪽 정렬 -> :<10 표현식을 사용하면 치환되는 문자열을 왼쪽으로 정렬하고 문자열의 총 자릿수를 10으로 맞출 수 있다. 
"{0:<10}".format("hi")
# 8. 오른쪽 정렬 :> 표현식을 사용하면 된다. 
"{0:>10}".format("hi")
# 9. 가운데 정렬 :^
"{0:^10}".format("hi")
# 10. 공백 채우기 채워 넣을 문자 값은 정렬문자 <,>,^바로 앞에 넣어야 한다.
"{0:=^10}".format("hi")
"{0:!<10}".format("hi")
# 11. 소수점 표현하기
# 12. {또는} 문자 표현하기
y = 3.42134234
"{0:0.4f}".format(y)
"{0:10.4f}".format(y)
# {또는} 문자 표현하기 
# {} 와 같은 중괄호 문자를 포매팅 문자가 아닌 문자 그대로 사용하고 싶은 경우에는 {{ }} 처럼 2개를 연속으로 사용하면 된다.
"{{and}}".format()
# 13. f 문자열 포매팅
name = '홍길동'
age = 30
f'나의 이름은 {name}입니다. 나이는 {age}입니다.'
