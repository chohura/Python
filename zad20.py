'''Zaimplementuj prosty problem pięciu filozofów (z deadlockiem), następnie usuń deadlock.
'''

import threading
import time

class Fork(threading.Semaphore):

    def take_semaphor(self):
        locked = self.acquire(False)
        if locked:
            return
        else:
            raise ResourceWarning

class Filozof(threading.Thread):
    running = True

    def __init__(self, index, leftFork, rightFork):
        threading.Thread.__init__(self)
        self.index = index
        self.leftfork = leftFork
        self.rightfork = rightFork

    def start(self):
        while self.running:
            time.sleep(10)
            print(f"Filozof {self.index} próbuje jeść\n")
            self.proba()

    def proba(self):
        fork1, fork2 = self.leftfork, self.rightfork
        while self.running:
            try:
                fork1.take_semaphor()
            except ResourceWarning:
                continue
            else:
                try:
                    fork2.take_semaphor()
                except ResourceWarning:
                    fork1.release()
                else:
                    break

        self.eat()
        fork1.release()
        fork2.release()
        self.running = False

    def eat(self):
        print(f"Filozof {self.index} zaczyna jesc\n")
        time.sleep(10)
        print(f"Filozof {self.index} konczy jesc\n")


if __name__ == '__main__':
    forks = [Fork() for _ in range(5)]

    filozofowie = [Filozof(i, forks[i % 5], forks[(i + 1) % 5])
                    for i in range(5)]

    Filozof.running = True
    for f in filozofowie:
        f.start()
    time.sleep(50)
    Filozof.running = False
    print("Koniec\n")