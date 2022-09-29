# 리스트를 복사할 때
# b는 a와 완전히 동일하다. 
a = [1,2,3]
b = a
id(a)
id(b)
# 값 하나를 변경했을 때

# 리스트를 복사할 때
# 1. [:] 사용 -> 리스트 전체를 가리키는 [:] 사용해서 복사한다.
# a리스트의 값을 바꾸더라도 b리스트에는 영향을 끼치지 않는다. 
a = [1,2,3]
b = a[:]
a[1] = 4
a
b
# 2. copy 모듈 사용
from copy import copy
a = [1,2,3]
b = copy(a)
b
b is a # b와 a가 가리키는 객체는 서로 다르다.

# 변수를 만드는 여러 가지 방법
a,b = ('python','life')
(a,b) = 'python', 'life'
[a,b] = ['python', 'life']
a = b = 'python'
