# 입력과 출력을 생각한다. 
# def GuGu(n):
#     # print(n)
#     result = []
#     result.append(n*1)
#     result.append(n*2)
#     result.append(n*3)
#     result.append(n*4)
#     result.append(n*5)
#     result.append(n*6)
#     result.append(n*7)
#     result.append(n*8)
#     result.append(n*9)
#     return result
def GuGu(n):
    # print(n)
    result = []
    i = 1
    while i < 10:
        result.append(n*i)
        i = i +1
    return result


print(GuGu(2))