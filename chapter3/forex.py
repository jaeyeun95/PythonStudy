# for 반복문
# 1. 전형적인 for문
from unittest import result


test_list = ['one','two','three']
for i in test_list:
    print(i)
# 2. 다양한 for문의 사용
a = [(1,2), (3,4), (5,6)]
for (first, last) in a:
    print(first + last)
# 3. for문의 응용
# 총 5명의 학생이 시험을 보았는데 시험 점수가 60점이 넘으면 합격이고 그렇지 않으면 불합격이다.
# 합격인지 불합격인지 결과를 보여 주시오.
marks = [90, 25, 67, 45, 80]
number = 0 # 학생에게 붙여 줄 번호
for mark in marks:
    number = number + 1
    if mark >= 60:
        print("%d번 학생은 합격입니다." % number)
    else:
        print('%d번 학생은 불합격입니다.' % number)
# for문과 continue문
marks = [90, 25, 67, 45, 80]
for mark in marks:
    number = number + 1
    if mark < 60: continue
    print('%d번 학생은 합격입니다.' % number)
# for문과 자주 함께 사용되는 range 함수
a = range(0, 10)
a
add = 0
for i in range(1, 11):
    add = add + i
print(add)
# 구구단
# 매개변수 end를 넣어 준 이유는 해당 결과값을 출력할 때 다음줄로 넘기지 않고 그 줄에 계속해서 출력하기 위해서이다.
for i in range(2, 10):
    for j in range(1,10):
        print(i*j, end = " ")
    print('')
# 리스트 내포 사용하기
# a리스트 각 항목에 3을 곱한 결과를 result 리스트에 담기
a = [1,2,3,4]
result = []
for num in a:
    result.append(num*3)
print(result)
# 리스트 내포 사용하기
a = [1,2,3,4]
result = [num * 3 for num in a]
print(result)