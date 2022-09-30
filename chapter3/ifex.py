# if 조건문
money = False
if money:
    print("택시를")
    print("타고 가라")
else:
    print("걸어가라")
    
# 비교 연산자 -> 만약 3000원 이상의 돈을 가지고 있으면 택시를 타고 그렇지 않으면 걸어 가라
money = 2000
if money > 3000:
    print("택시를 타고 가라")
else:
    print('걸어가라')
    
# and, or, not 연산자 -> 3000원 이상의 돈이 있거나 카드가 있다면 택시를 타고 그렇지 않으면 걸어 가라
money = 2000
card = False
if money >= 3000 or card:
    print("택시를 타고 가라")
else:
    print('걸어가라')
    
# x in s, x not in s -> s 안에 x가 있는지, 없는지
1 in [1,2,3]    #-> 리스트
'a' in ('a','b','c')    # -> 튜플

# 만약 주머니에 돈이 있으면 택시를 타고, 없으면 걸어 가라
pocket = ['knife', 'phone', 'card']
if 'card' in pocket:
    print("택시를 타고 가라")
else:
    print('걸어가라')
    
# 조건문에서 아무 일도 일어나지 않게 설정하려면 -> pass사용
pocket = ['knife', 'phone', 'card']
if 'card' in pocket:
    pass
else:
    print('걸어가라')
    
# 다양한 조건을 판단하는 elif
# 주머니에 돈이 있으면 택시를 타고, 주머니에 돈은 없지만 카드가 있으면 택시를 타고, 돈도 없고 카드도 없으면 걸어가라
# if 문만 사용해서
pocket = ['paper', 'cellphone']
card = True
if 'money' in pocket:
    print('택시를 타고 가라')
else:
    if card:
        print('택시를 타고 가라')
    else:
        print('걸어 가라')
# elif 사용했을 때
if 'money' in pocket:
    print('택시를 타')
elif card:
    print('택시를 타')
else:
    print('걸어가')

# if문 한 줄로 작성하기
if 'money' in pocket: pass
else: print('카드를 꺼내')

# 조건부 표현식
# 조건문이 참인 경우 if 조건문 else 조건문이 거짓인 경우
score = 70
if score >= 60:
    message = 'success'
else:
    message = 'failure'
message
#  조건부 표현식을 사용하면
message = 'success' if score >- 60 else 'failure'
message
