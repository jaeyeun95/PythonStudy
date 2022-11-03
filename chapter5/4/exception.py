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

# 오류 일부러 발생시키기 -> raise 명령어 사용
class Bird:
    def fly(self):
        # raise NotImplementedError
        print('very fast')

class Eagle(Bird):
    pass

eagle = Eagle()
eagle.fly()
# 예외 만들기
class MyError(Exception):
	pass
def say_nick(nick):
    if nick == '바보':
        raise MyError()
    print(nick)

try:    
    say_nick("천사")
    say_nick('바보')
except MyError:
    print('허용되지 않는 별명입니다.')