from concurrent.futures import ProcessPoolExecutor
from multiprocessing import Process
# def worker():
#     print("Worker process running")
# process = Process(target=worker)
# process.start()
# process.join()
# print("Main process finished")

def square(x):
    return x*x
if __name__ == "__main__":
    with ProcessPoolExecutor(max_workers=4) as executor:
        results = list(executor.map(square,range(10)))
        print(results)