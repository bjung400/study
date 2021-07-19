import time
import threading

def long_task():
    for i in range(1,6):
        time.sleep(1)
        print("working:%s\n" % i)

print("Start")

threads = []
for i in range(5):
    # Thread 생성
    t = threading.Thread(target=long_task)

    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join()

print("End")
