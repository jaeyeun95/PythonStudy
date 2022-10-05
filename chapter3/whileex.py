# while 반복문
# 열 번 찍어 안 넘어가는 나무 없다 속담을 파이썬으로 표현하면
treeHit = 0
while treeHit < 10:
    treeHit = treeHit +1
    print("나무를 %d번 찍었습니다." % treeHit)
    if treeHit == 10:
        print('나무 넘어갑니다.')

# 여러 가지 선택지 중 하나를 선택해서 입력받는 예제를 만들어 보자.
prompt = """
1. Add
2. Del
3. List
4. Quit
Enter number:"""

number = 0
while number != 4:
    print(prompt)
    number = int(input())
    
# 커피 자판기에서 커피가 다 떨어졌을 때 판매중지 
coffee = 10
money = 300
while money:
    print('돈을 받았으니 커피를 줍니다.')
    coffee = coffee -1
    print('남은 커피의 양은 %d개 입니다.' % coffee)
    if coffee == 0:
        print('커피가 다 떨어져서 판매를 중지합니다.')
        break

# continue
a = 0
while a < 10:
    a = a + 1
    if a % 2 == 0: continue
    print(a)

# 무한 루프
while True:
    print("Ctrl+C를 눌러야 while문을 빠져나갈 수 있습니다.")