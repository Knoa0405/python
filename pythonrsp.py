import random

rocksp = ['가위','바위','보']
a = random.choice(rocksp)
c =['가위','바위','보']
input('게임을 시작한다.enter 시작!')


x = input("나 : ")

if x in c :
  e = c.index(x) + 1
else :
  print('가위 바위 보만 입력해주세요!')

print("john : " + a)

if x :
  d = rocksp.index(a) + 1

if e == d :
  print('비김')
  
if e == 1 :
  if d == 2 :
    print('John 승리')
  elif d == 3 :
    print('나의 승')

elif e < d :
  print('john 승리')

elif e > d :
  print('나의 승리')

elif e == 3 :
    
  if d == 1 :
    print('john 승')
  elif d == 2 :
    print('나의 승')