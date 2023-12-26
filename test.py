import mod1
#import mod1 as md          -> md 로 이름해서 쓰겠다.
#from mod1 import *         -> 다 가져와 mod1(파일)명 생략하겠다.
#from mod1 import add, sub  -> 요것만 가져와 mod1(파일)명 생략하겠다.

print(mod1.add(100, 200))
print(mod1.sub(100, 200))
#print(md.add(100, 200))
#print(add(100, 200))
#print(add(100, 200))
print(mod1.pp)

