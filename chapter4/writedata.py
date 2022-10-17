f = open('새파일.txt', 'w')
for i in range(1, 11):
    data = '%d번째 줄입니다.\n' % i
    f.write(data)
f.close()

# readlines 사용
f = open('새파일.txt', 'r')
lines = f.readlines()
for line in lines:
    print(line)
f.close()
# read 사용
f = open('새파일.txt', 'r')
data = f.read()
print(data)
f.close()
# 파일 내용 추가하기
f = open('새파일.txt', 'a')
for i in range(11, 20):
    data = '%d 번째 줄입니다. \n' %i
    f.write(data)
f.close()
# with 문과 함께 사용하기
f = open('foo.txt', 'w')
f.write('Life is too short, you need python')
f.close()
with open('foo1.txt', 'w') as f:
    f.write('Life is too short, you need python')
    
# p176 해야함