# 딕셔너리 자료형 -> Key : Value 형식으로 되어 있음 , 자바에서의 map
# value에 리스트 또한 넣을 수 있다. 
from re import A


a = {1: 'hi'}
b = {'b' : [1,2,3]}

# 딕셔너리 쌍 추가, 삭제하기
# 1. 딕셔너리 쌍 추가하기
a = {1: 'a'}
a[2] = 'b'
a['name'] = 'pey'
a
# 2. 딕셔너리 요소 삭제하기 
del a[1]
a

# 딕셔너리 활용하기
# Key를 사용해 Value 얻기
# 딕셔너리는 리스트나 튜플에 있는 인덱싱 방법을 사용할 수 없다. 
grade = {'pey':10, 'juliet':99}
grade['pey']
grade['juliet']

# - 딕셔너리 만들 때 주의할 사항 -> Key는 고유한 값이므로 중복되는 Key값을 설정해 놓으면 하나를 제외한 나머지 것들이 모두 무시된다는 점을 주의해야 한다.
# Key 값에 리스트를 사용할 수 없다.
a = {1:'a',1:'b'}
a

# 딕셔너리 관련 함수
# Key 리스트 만들기(keys)
a = {'name' :'pey', 'phone':'0101234', 'birth': '1118'}
a.keys()
# dict_keys 객체는 리스트를 사용하는 것과 차이가 없지만, 리스트 고유의 함수는 수행할 수 없다.
for k in a.keys():
    print(k)
# dict_keys 객체 -> list
list(a.keys())
# Value 리스트 만들기
a.values()
# Key, Value 쌍 얻기(items)
a.items()
# Key:Value 쌍 모두 지우기(clear)
a.clear()
a
# Key로 Value 얻기(get)
a.get('name')
# 딕셔너리 안에 찾으려는 Key 값이 없을 경우 미리 정해 둔 디폴트 값을 대신 가져오게 하고 싶을 때는
# get(x, '디폴트 값')을 사용하면 편리하다. 
a.get('foo', 'bar')
# 해당 Key가 딕셔너리 안에 있는지 조사하기(in)
'name' in a
'name' in b