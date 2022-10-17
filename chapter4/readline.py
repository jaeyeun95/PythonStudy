f = open('새파일.txt', 'r')
line = f.readline()
print(line)
f.close()

# 모든 line 읽어오기
f = open('새파일.txt', 'r')
while True:
    line = f.readline()
    if not line: break    
    print(line)
f.close()

while 1:
    data = input()
    if not data: break
    print(data)
    