import threading
import random

a1 = random.randint(1, 8)
a2 = random.randint(1, 8)
a3 = random.randint(1, 8)
a4 = random.randint(1, 8)
a5 = random.randint(1, 8)


def fun():


    [x for x in range(10000000)]


t1 = threading.Thread(args=(), target=fun)
t2 = threading.Thread(args=(), target=fun)
t3 = threading.Thread(args=(), target=fun)
t4 = threading.Thread(args=(), target=fun)
t5 = threading.Thread(args=(), target=fun)

t1.start()
print('start t1', a1)
t2.start()
print('start t2', a2)
t3.start()
print('start t3', a3)
t4.start()
print('start t4', a4)
t5.start()
print('start t5', a5)

t5.join()
print('koniec 5')
t4.join()
print('koniec 4')
t3.join()
print('koniec 3')
t2.join()
print('koniec 2')
t1.join()
print('koniec 1')


