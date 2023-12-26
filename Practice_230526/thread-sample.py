import threading
import time

def worker1(x1, x2):
    while x2 > 0:
        print(f'sub thread: {x1} [{x2}]\n')
        time.sleep(1)
        x2 -= 1

def worker2(x1, x2):
    while x2 > 0:
        print(f'sub thread: {x1} [{x2}]\n')
        time.sleep(1)
        x2 -= 1

t1 = threading.Thread(target = worker1, args = ("designer", 20))
t2 = threading.Thread(target = worker2, args = ("programmer", 10))

## daemon은 메인 스레드가 끝나면 같이 끝난다.
## daemon은 start 전에 설정해주는 방식
# t1.daemon = True
# t2.daemon = True

## join은 메인스레드가 서브 스레드가 모두 종료될 때까지 기다려줌
## join은 start 후에 설정해주는 방식
t1.start()
t1.join()
t2.start()
t2.join()

print('main thread')