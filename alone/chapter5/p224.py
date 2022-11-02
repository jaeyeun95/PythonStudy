# IndexError가 발생할 때 오류 메세지를 출력하는 소스를 작성해 보자
a = [1,2,3]
try: 
    a[4]
except IndexError as e:
    print(e)
