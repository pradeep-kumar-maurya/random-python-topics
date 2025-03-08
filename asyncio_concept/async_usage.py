# subroutine execution can't be pasued and resumed. subroutins is a subset of a larger program.
# coroutine execution can be pasued and resumed. Suitable for I/O operations, DB queries, HTTP Requests.
# coroutine makes asynchronous/concurrent execution possible.


import asyncio, time

async def brewCoffee():
    print("start coffee")
    # time.sleep(3)  # blocking I/O operation, can't be awaited
    await asyncio.sleep(3)  # non-blocking I/O operation which can be awaited
    print("end coffee")
    return "coffee done"


async def toastBagel():
    print("start toast")
    await asyncio.sleep(2)  # non-blocking I/O operation which can be awaited
    print("end toast")
    return "toast done"


async def main():
    s = time.time()

    # below we create task in batches
    # batch = asyncio.gather(brewCoffee(), toastBagel())
    # result_coffee, result_bagel = await batch

    # below we create individual task and then run the coroutine
    coffee_task = asyncio.create_task(brewCoffee())
    toast_task = asyncio.create_task(toastBagel())
    result_coffee = await coffee_task
    result_bagel = await toast_task

    e = time.time()
    elapsed_time = e - s

    print(result_coffee)
    print(result_bagel)
    print(f'elapsed time: {elapsed_time:.2f} secs')


if __name__ == '__main__':
    asyncio.run(main())



