import threading
import random
import time


def foo():
    print('poczatek pracy')
    spanko = random.randint(1, 8)
    time.sleep(spanko)
    print('koniec pracy')


t1 = threading.Thread(target=foo, args=())
t2 = threading.Thread(target=foo, args=())
t3 = threading.Thread(target=foo, args=())
t4 = threading.Thread(target=foo, args=())
t5 = threading.Thread(target=foo, args=())

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