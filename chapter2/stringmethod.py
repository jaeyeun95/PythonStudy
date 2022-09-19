# 문자열 관련 함수
# 문자 개수 세기(count)
a = 'hobby'
a.count('b')
# 2. 위치 알려주기 1(find)
a = 'Python is the best choice'
a.find('b')  # 문자열에서 'b'가 처음 나온 위치
# 3. 위치 알려주기 2(index)
a = 'Life is too short'
a.index('t')  # 문자열에서 t가 처음 나온 위치를 반환한다. 만약 찾는 문자가 없으면 오류를 발생시킨다.
# 4. 문자열 삽입(join) -> 각각의 문자 사이에 ","를 삽입한다. 
",".join('abcd')
# 5. 소문자를 대문자로 바꾸기(upper)
a = 'hi'
a.upper()
# 6. 대문자를 소문자로 바꾸기(lower)
a = 'HI'
a.lower()
# 7. 왼쪽 공백 지우기(lstrip)
a = ' HI '
a.lstrip()
# 8. 오른쪽 공백 지우기(rstrip)
a = 'hi '
a.rstrip()
# 9. 양쪽 공백 지우기(strip)
a = ' hi'
a.strip()
# 10. 문자열 바꾸기(replace)
a = 'Life is too short'
a.replace('Life', 'Your leg')
# 11. 문자열 나누기(split)
a = 'Life is too short'  
a.split()  # 공백을 기준으로 문자열 나눔
b = "a:b:c:d"
b.split(':')  # :기호를 기준으로 문자열 나눔