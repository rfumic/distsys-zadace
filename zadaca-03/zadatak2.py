import asyncio
from time import sleep
import numpy as np
import psutil


async def afunc1():
    for i in range(10):
        np.random.normal(loc=0, scale=1, size=1000000)
        sleep(0.9)


async def afunc2():
    return psutil.cpu_percent(10)


async def main():
    await afunc1()
    cpu = await afunc2()
    print("Iskorištenost CPU u 10 sekundi iznosi : ", cpu)


if __name__ == "__main__":
    asyncio.run(main())
