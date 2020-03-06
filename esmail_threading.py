#!/usr/bin/env python
from threading import Thread, Lock
import time

task_lock = Lock()

def task1(check_point):
    task_lock.acquire()
    for i in range(10):
        print("task1:", i)
        time.sleep(.5)
        if i == check_point:
            task_lock.release()

def task2(check_point):
        task_lock.acquire()
        for i in range(10):
            print("task2:", i)
            if i == check_point:
                task_lock.release()

t1 = Thread(target=task1, args=(4,))
t2 = Thread(target=task2, args=(7,))

t1.start()
t2.start()
