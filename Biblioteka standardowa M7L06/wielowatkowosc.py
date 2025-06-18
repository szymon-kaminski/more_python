import threading
import time

def worker():
    print("Wątek stratuje")
    time.sleep(2)
    print("Wątek kończy")


t = threading.Thread(target=worker)

t.start()

t.join()
time.sleep(2)
print("Główny wątek kończy się")

########################################################################
########################################################################
import threading
import time

def print_numbers(n):
    for i in range(n):
        print(f"{threading.current_thread().name}: {i}")
        time.sleep(0.5)

threads = []
for i in range(3):
    t = threading.Thread(target=print_numbers, args=(3,), name=f"Wątek-{i}")
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("Wszystkie wątki zakończone")

###############################################################
###############################################################

import threading
import time

class MyThread(threading.Thread):
    def run(self):
        print(f"{self.name} działa")
        time.sleep(1)
        print(f"{self.name} kończy")

t1 = MyThread()
t2 = MyThread()

t1.start()
t2.start()

t1.join()
t2.join()

###################################################################
###################################################################
import threading

counter = 0
lock = threading.Lock()

def add():
    global counter
    for _ in range(100_000):
        with lock:  # Bez tego wartość może być błędna!
            counter += 1

t1 = threading.Thread(target=add)
t2 = threading.Thread(target=add)

t1.start()
t2.start()
t1.join()
t2.join()

print("Wynik końcowy:", counter)
