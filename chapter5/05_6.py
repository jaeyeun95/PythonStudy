# pickle -> 객체의 형태를 그대로 유지하면서 파일에 저장하고 불러올 수 있게 하는 모듈이다. 
import pickle
f = open('test.txt', 'wb')
data = {1:'python', 2: 'you need'}
pickle.dump(data, f)
f.close

# shutil -> 파일을 복사해주는 파이썬 모듈
import shutil
shutil.copy('test.txt', 'dst.txt')

# calendar -> 달력을 볼 수 있게 해주는 모듈
import calendar
print(calendar.calendar(2022))

# random
import random
random.random()
# webbrowser
import webbrowser
webbrowser.open('https://google.com')