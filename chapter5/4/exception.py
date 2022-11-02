# 예외 처리
f = open('없는 파일', 'r')
4 / 0
a = [1,2,3]
a[4]
# try, exception 문
# try:
# 	...
# exception [발생오류[as 오류 메시지 변수]]:
# 	...

try:
    4 / 0
except ZeroDivisionError as e:
    print(e)
    
# finally
f = open('foo.txt', 'w')
try:
    print('finally test')
finally:
    f.close()
    
# 여러 개의 오류 처리하기
try:
    a = [1,2]
    print(a[3])
    4/0
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다.')
except IndexError:
    print('인덱싱 할 수 없습니다.')
# exception 에 한번에 같이 사용할 수 있다.
try:
    a = [1,2]
    print(a[3])
    4/0
except (ZeroDivisionError, IndexError) as e:
    print(e)
# 오류 회피하기
try:
    f = open('dddd', 'r')
except FileNotFoundError:
    pass