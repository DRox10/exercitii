'''
import asyncio
import time

async def functie():
    print("1 - A")
    # await time.sleep(2)
    await asyncio.sleep(0)
    print("1 - B")

async def o_alta_functie():
    print("2 - A")
    # await functie()
    task = asyncio.create_task(functie())
    # print(task)
    await asyncio.sleep(0)
    print("2 - B")
    await task

async def trei_in_paralel():
    await asyncio.gather(functie(), functie(), functie())

asyncio.run(trei_in_paralel())
'''

#un program care sa intoarca 3 nr:
#intre 0-1000, 1000-10000, 10000-100000

import time

def este_prim(numar):
    for i in range(2, numar):
        if numar % 1 == 0:
            return False
    return True

def cel_mai_mare(start, end):
    for i in range(end, start, -1):
        if este_prim(i):
            return i

def calcul_sincron():
    x = cel_mai_mare(0, 1000)
    print(x)
    y = cel_mai_mare(1000, 10000)
    print(y)
    z = cel_mai_mare(10000, 100000)
    print(z)

if __name__ == "__main__":
    time1 = time.time()
    calcul_sincron()
    time2 = time.time()
    print(f"Functia sincrona a durat {time2-time1}")

