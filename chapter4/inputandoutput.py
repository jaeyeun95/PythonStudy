# 04-2. 사용자 입력과 출력
# 사용자가 입력한 값을 어떤 변수에 대입하고 싶을 떄
# input 사용
a = input()

number = input("숫자를 입력해주세요: ")
# print 자세히 알기
a = 123
print(a)

# print 자세히 알기
# 큰 따옴표(”)로 둘러싸인 문자열은 + 연산과 동일하다.
print("Life" "is" "too short")
print("life" + 'is' + 'too short')
# 문자열 띄어쓰기는 콤마로 한다.
print('life', 'is', 'too short')
# 한줄에 결과값 출력하기
for i in range(10):
    print(i, end=' ')