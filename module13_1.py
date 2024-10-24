import time
import asyncio

async def start_strongman(name, power):
    print(f"{name} начал соревнование.")
    for i in range(1, 6):
        await asyncio.sleep(1 / power)
        print(f"Силач {name} поднял {i}")

    
    print(f"Силач {name} закончил соревнование")

async def start_tournament():
    task1 = asyncio.create_task(start_strongman('Palev', 3))
    task2 = asyncio.create_task(start_strongman('Igor', 2))
    task3 = asyncio.create_task(start_strongman('Appolon', 5))

    await task1
    await task2
    await task3




asyncio.run(start_tournament())
