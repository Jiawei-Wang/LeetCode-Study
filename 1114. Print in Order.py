# 3 threads
# each thread calls one method
# threads can start in any order
# but output must always be: first, second, third



# Barrier: A Barrier blocks threads at a checkpoint until a fixed number of threads arrive, then releases all of them together.
# threads wait until a specified number of threads reach the same point
# then all of them are released together
# (no one moves forward until everyone arrives)
from threading import Barrier

class Foo:
    def __init__(self):
        self.first_barrier = Barrier(2) # two threads must call .wait()
        self.second_barrier = Barrier(2)


    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.first_barrier.wait() 
        # if first() is called before second():
        # printFirst() is executed
        # first_barrier reaches 1/2
        # when second() is called:
        # first_barrier reaches 2/2
        # printSecond() is executed
        # 
        # if second() is called before first():
        # first_barrier reaches 1/2
        # printSecond() is blocked
        # when first() is called:
        # printFirst() is executed
        # first_barrier reaches 2/2 
        # printSecond() is executed
        #
        # so printFirst() will always go before printSecond()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        
        # printSecond() outputs "second". Do not change or remove this line.
        self.first_barrier.wait()
        printSecond()
        self.second_barrier.wait()
        # same logic for second_barrier:
        # if third() -> second() -> first():
        # second_barrier blocks, first_barrier blocks, printFirst() is executed, then printSecond(), then printThird()


    def third(self, printThird: 'Callable[[], None]') -> None:
        
        # printThird() outputs "third". Do not change or remove this line.
        self.second_barrier.wait()
        printThird()


# Lock: a lock is of binary state: locked/unlocked, 
# only one thread can hold it at a time
# other threads can't move until it's released
# (think of it as only one thread may pass the door)
from threading import Lock

class Foo:
    def __init__(self):
        self.locks = (Lock(),Lock()) # create two locks
        self.locks[0].acquire() # lock first one
        self.locks[1].acquire() # lock second one
        # two doors are closed and no thread owns the doors

    def first(self, printFirst):
        printFirst()
        self.locks[0].release()
        # python lock object doesn't track ownership
        # any thread can release a lock even if it didn't acquire it
        # in this case: first() never acquired the lock but can release it
        

    def second(self, printSecond):
        with self.locks[0]: # attemps to acquire first lock
            # if lock is unlocked: any thread can acquire it
            # if lock is locked: it needs to be released first to be acquired by a thread
            # if first lock is not released yet: can't execute
            # if first lock is released: can execute
            printSecond()
            self.locks[1].release()
            
            
    def third(self, printThird):
        with self.locks[1]:
            printThird()


# TODO: next 3 solutions:


from threading import Event

class Foo:
    def __init__(self):
        self.done = (Event(),Event())
        
    def first(self, printFirst):
        printFirst()
        self.done[0].set()
        
    def second(self, printSecond):
        self.done[0].wait()
        printSecond()
        self.done[1].set()
            
    def third(self, printThird):
        self.done[1].wait()
        printThird()


from threading import Semaphore

class Foo:
    def __init__(self):
        self.gates = (Semaphore(0),Semaphore(0))
        
    def first(self, printFirst):
        printFirst()
        self.gates[0].release()
        
    def second(self, printSecond):
        with self.gates[0]:
            printSecond()
            self.gates[1].release()
            
    def third(self, printThird):
        with self.gates[1]:
            printThird()


from threading import Condition

class Foo:
    def __init__(self):
        self.exec_condition = Condition()
        self.order = 0
        self.first_finish = lambda: self.order == 1
        self.second_finish = lambda: self.order == 2

    def first(self, printFirst):
        with self.exec_condition:
            printFirst()
            self.order = 1
            self.exec_condition.notify(2)

    def second(self, printSecond):
        with self.exec_condition:
            self.exec_condition.wait_for(self.first_finish)
            printSecond()
            self.order = 2
            self.exec_condition.notify()

    def third(self, printThird):
        with self.exec_condition:
            self.exec_condition.wait_for(self.second_finish)
            printThird()