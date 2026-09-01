from concurrent.futures import ThreadPoolExecutor

def square(x):
    return x*x

with ThreadPoolExecutor(max_workers=4) as executor:
    # results = list(executor.map(square,range(10)))
    future  = executor.submit(square,10)
    results = future.result()
    futures = [ executor.submit(square,i) for i in range(10) ]
for i in futures:
    print(i.result())