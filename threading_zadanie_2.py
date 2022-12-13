import threading
import random
import time


def foo(*args):
    print('start' f'{args}')
    spanko = random.randint(1, 8)
    time.sleep(spanko)
    print('koniec pracy' f'{args}')


t1 = threading.Thread(target=foo, args=('thread no 1', ))
t2 = threading.Thread(target=foo, args=('thread no 2', ))
t3 = threading.Thread(target=foo, args=('thread no 3', ))
t4 = threading.Thread(target=foo, args=('thread no 4', ))
t5 = threading.Thread(target=foo, args=('thread no 5', ))

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()

print('==')

t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
print('KONIEC')