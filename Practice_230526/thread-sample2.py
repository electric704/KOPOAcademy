import threading
import time

num = 0
lock = threading.Lock()
lock = threading.Semaphore(5)
## mutax -> 자원을 다 쓸 때까지 프로세스 하나씩 기다림
## Semaphore -> 받은 인자받음 만큼 여러 개의 프로세스가 기다림
## Critical Section -> 임계영역, 스레드 연산 중 메모리를 공유함

print(type(lock))

def worker1(x1, x2):
    global num
    
    while x2 > 0:
        print(f'sub thread: {x1} [{x2}]\n')
        lock.acquire()
        time.sleep(1)
        x2 -= 1; num +=1
        print(f'num1 : [{num}]\n')
        lock.release()

def worker2(x1, x2):
    global num
    
    while x2 > 0:
        print(f'sub thread: {x1} [{x2}]\n')
        lock.acquire()
        time.sleep(1)
        x2 -= 1; num +=1
        print(f'num2 : [{num}]\n')
        lock.release()

t1 = threading  .Thread(target = worker1, args= ("designer", 20))
t2 = threading  .Thread(target = worker2, args= ("programmer", 10))
t1.start()
t2.start()
print('main thread')