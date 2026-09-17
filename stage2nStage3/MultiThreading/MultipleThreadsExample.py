import threading 
import time

def worker(name):
    print(f"{name} started")
    time.sleep(2)
    print(f"{name}finished")
threads=[]
for i in range(3):
    thread = threading.Thread(
        target=worker,
        args=(f"Thread-{i}",)
    )
    thread.start()
    threads.append(thread)
    
for thread in threads:
    thread.join()