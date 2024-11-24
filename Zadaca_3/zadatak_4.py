import asyncio
import random

async def provjeri_parnost(x):

    await asyncio.sleep(2)
    if x%2==0:
         return f"Broj {x} je paran"
    else:
        return f"Broj {x} je neparan"
    
async def main():
    lista_brojeva = [random.randint(1,100) for i in range(1,11)]
    zadaci = [asyncio.create_task(provjeri_parnost(lista_brojeva[x])) for x in range(0,10)]
    rezultati =await asyncio.gather(*zadaci)
    print(rezultati)
    
asyncio.run(main())