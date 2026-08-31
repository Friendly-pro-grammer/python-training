import asyncio

async def hello():
    print("hello")
# result = hello()
##not immediate result but returns a coroutine object
# print(result)
#A coroutine is an asynchronous computation that can be paused and resumed.
async def dowload_data():
    print("Downloading")
    await asyncio.sleep(2)
    print("Download complete")
asyncio.run(dowload_data())
async def task(name, delay):
    print(f"{name} started")
    await asyncio.sleep(delay)
    print(f"{name} finished")
    
async def main():
    await asyncio.gather(
        task("A",2),
        task("B",2),
        task("C",2),
        task("D",2)
    )
asyncio.run(main())

