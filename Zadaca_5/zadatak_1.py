import asyncio
import aiohttp
from aiohttp import web

app= web.Application()

def handler_function(request):
    data = {
        "naziv": "kruh",
        "cijena": 5,
        "količina": 3
    }
    return web.json_response(data)


app.router.add_get("/proizvodi", handler_function)



web.run_app(app, host="localhost",port=8080)

