import asyncio
from time import sleep
import os


async def afun1(lista):
    sleep(0.2)
    return [{"naziv": d, "velicina": os.stat(d).st_size} for d in lista]


def fun2(lista):
    for d in lista:
        f = open(d, "a")
        for n in range(1, 10000):
            f.write(str(n))
        f.close()


async def main():
    datoteke = ["datoteka1", "datoteka2", "datoteka3"]
    for d in datoteke:
        open(d, "w")

    x = asyncio.create_task(afun1(datoteke))
    fun2(datoteke)
    rezultat = await asyncio.gather(x)
    print(rezultat)


if __name__ == "__main__":
    asyncio.run(main())
