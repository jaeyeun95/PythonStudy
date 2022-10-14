# 함수 안에서 선언한 변수의 효력 범위
a = 1
def vartest(a):
    a = a + 1

vartest(a)
print(a)
