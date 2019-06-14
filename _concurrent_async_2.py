import time
import asyncio
import uvloop


async def say_after(delay, what):
    await asyncio.sleep(delay)
    for i in range(10000):
        pass
    return what


async def main():
    print(f"started at {time.strftime('%X')}")
    tasks = [say_after(1, "hello"), say_after(5, "world"), say_after(1, "again")]
    items = await asyncio.gather(*tasks)
    print(items)
    print(f"finished at {time.strftime('%X')}")


uvloop.install()
asyncio.run(main())
