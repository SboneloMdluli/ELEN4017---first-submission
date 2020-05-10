#!/usr/bin/python
import threading
import time

exitFlag = 0

class myThread(threading.Thread):

    def __init__(self, threadID, name, counter, delay):

        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.delay = delay


    def run(self):

        print("Starting " + self.name)
        print(self)
        print_time(self.name, self.counter, self.delay)
        print("Exiting " + self.name)


def print_time(threadName, counter, delay):

    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print("%s: %s %d" % (threadName, time.ctime(time.time()), counter))
        print(threading.active_count())
        counter -= 1



# Create new threads

numThreads = 5
counters = [10, 3, 5, 3, 4]
threads = []

# create new threads
for i in range(numThreads):
    t = myThread(i+1, "Thread-{}".format(i+1), counters[i], i+1)
    threads.append(t)

# Start new Threads
for i in range(numThreads):
    threads[i].start()
print("Exiting Main Thread")

