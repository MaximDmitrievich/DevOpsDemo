from aiohttp import web
from os import environ

async def hello(request):
    return web.Response(text="Hello, world")

app = web.Application()
app.add_routes([web.get('/', hello)])

web.run_app(app, host=environ["APP_HOST"], port=environ["APP_PORT"])