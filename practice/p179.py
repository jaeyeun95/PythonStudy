# Q1. 주어진 자연수가 홀수인지 짝수인지 판별해 주는 함수(is_odd)를 작성해 보자.
from unittest import result


def is_odd(number):
    if number % 1 == 0:
        return True
    else:
        return False

is_odd(5)

# Q2. 입력으로 들어오는 모든 수의 평균 값을 계산해 주는 함수를 작성해 보자. (단, 입력으로 들어오는 수의 개수는 정해져 있지 않다.)
def avg_numbers(**args):
    print('ddd',args)
    result = 0
    for i in args:
        result += i
    return result / len(args)

avg_numbers(1,2)
avg_numbers(1,2,3,4,5)