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


