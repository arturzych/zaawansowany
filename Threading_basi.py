import threading


def foo():
    [x for x in range(1000000)]
    print('*************')


t1 = threading.Thread(target=foo, args=())

t1.start()
print('==')

t1.join()
print('konczymy prace, wsyztskie watki zakonczone')