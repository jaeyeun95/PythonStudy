# 1 부터 10까지의 숫자 중에서 3의 배수를 뺀 나머지 값을 출력해보자
a = 0
while a < 10:
    a = a + 1
    if a % 3 == 0: continue
    print(a)