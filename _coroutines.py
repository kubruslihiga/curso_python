def coro():
    i = 0
    while i < 2:
        item = yield
        i += 1
        print(item)
        
c = coro()
next(c)
try:
    c.send("abc")
    c.send("abc 2")
    c.send("abc") # aqui dá erro!
    c.send("abc")
except StopIteration as si:
    print("ahhh mlq")


import asyncio

async def async_function():
    print('hello')
    #await asyncio.sleep(1)
    print('world')

asyncio.run(async_function())

import random

def producer(item):
    print(f'Producing item {item}')
    yield item

def consumer(name):
    call = 0
    while True:
        item = list((yield))[0]
        print(f'{name} n: {call} is doing work on item %s' % item)
        call += 1

messengers = [consumer('Consumer 1'), consumer('Consumer 2')]
next(messengers[0])
next(messengers[1])
for i in range(8):
    messenger = messengers[random.randint(0, 1)]
    item = producer(f'item: {i}')
    messenger.send(item)
