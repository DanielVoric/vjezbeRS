import asyncio

async def korutina():
    lista_brojeva = [i for i in range (1,11)]
    print(f'dohvacam listu brojeva ')
    await asyncio.sleep(3)
    print(f'Podaci dohvaceni: {lista_brojeva}')
    return lista_brojeva

asyncio.run(korutina())
    