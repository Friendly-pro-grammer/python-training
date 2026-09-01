import threading

def worker():
    print("hello worker running")
thread  = threading.Thread(target=worker)

print("before worker")
thread.start()
thread.join()
print("worker should've finished")  