import multiprocessing

manager = multiprocessing.Manager()
shared_list = manager.list()


def worker1(l, a, b, k):
    for i in range(a):
        l.append((k, i + b))


def worker2(l, b, c, k):
    for i in range(b):
        l.append((k, i + c))


a, b, c = 10, 20, 100
for i in range(5):
    process1 = multiprocessing.Process(target=worker1, args=[shared_list, a, b, i])
    process2 = multiprocessing.Process(target=worker2, args=[shared_list, b, c, i])
    process1.start()
    process2.start()
    process1.join()
    process2.join()
from pprint import pprint

pprint(sorted(shared_list))
##[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 5, 6, 7, 8]
