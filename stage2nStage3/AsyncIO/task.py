import asyncio
async def download():
    await asyncio.sleep(3)
    return "data"
async def main():
    task = asyncio.create_task(download())
    print("Doing some other work")
    result = await task
    print(result)
asyncio.run(main())

#common production pattern
# tasks = [
#     asyncio.create_task(job1()),
#     asyncio.create_task(job2()),
#     asyncio.create_task(job3())
# ]

# results = await asyncio.gather(*tasks)