import threading
import time
class DemoThread(threading.Thread):

    def __init__(self, nbIter, num, sleep, finishedCb, progressCb):
        super().__init__()
        self.nbIter = nbIter
        self.num = num
        self.sleep = sleep
        self.result = 1
        self.finishedCb = finishedCb
        self.progressCb = progressCb

    def run(self) -> None:
        for i in range(self.nbIter):
            self.result *= 2
            time.sleep(self.sleep)
            #print(f"{self.num}:{self.result}")
            if i % 7 == 0:
                self.progressCb(self.num, i / self.nbIter)
        self.finishedCb(self.num, self.result)

def finished(num, result):
    print(f"From thread {num} the main thread display the result is {result}")

def progress(num, completion):
    print(f"From thread {num} progress {completion * 100:.0f}%")

if __name__ == '__main__':
    t1 = DemoThread(100,1,0.06, finished, progress)
    t2 = DemoThread(50,2,0.1, finished, progress)
    t3 = DemoThread(75, 3, 0.09, finished, progress)
    t1.start()
    t2.start()
    t3.start()

