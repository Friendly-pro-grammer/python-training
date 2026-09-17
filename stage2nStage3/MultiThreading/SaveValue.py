import threading

results = []

def worker(value):
    results.append(value*2)

threads = [
    threading.Thread(target=worker,args=(i,))
    for i in range(5)
]

for t in threads:
    t.start()
for j in threads:
    j.join()
print(results)