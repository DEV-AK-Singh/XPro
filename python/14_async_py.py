# import time 
# def task():
#     print("Task started")
#     time.sleep(5)
#     print("Task completed")
# task()

# import asyncio
# async def taskX():
#     print("Task started X")
#     await asyncio.sleep(5)
#     print("Task completed X")
# async def taskY():
#     print("Task started Y")
#     await asyncio.sleep(2)
#     print("Task completed Y")
# asyncio.run(taskX())
# asyncio.run(taskY())

# import asyncio
# async def task(name, seconds):
#     print(f"{name} started")
#     await asyncio.sleep(seconds)
#     print(f"{name} finished")
# async def main():
#     # await task("A", 2)
#     # await task("B", 2)
#     # await task("C", 2)
#     await asyncio.gather(task("A", 3), task("B", 2), task("C", 1))
# asyncio.run(main())

# import asyncio
# async def main():
#     task1 = asyncio.create_task(task("A", 3))
#     task2 = asyncio.create_task(task("B", 2))
#     task3 = asyncio.create_task(task("C", 1))
#     await asyncio.gather(task1, task2, task3)
# async def task(name, seconds):
#     print(f"{name} started")
#     await asyncio.sleep(seconds)
#     print(f"{name} finished")
# asyncio.run(main())

class Resource: 
    async def __aenter__(self):
        print("Opening")
        return self 
    async def __aexit__(self, exc_type, exc, tb):
        print("Closing")
async def main():
    async with Resource() as resource:
        print("Using resource")