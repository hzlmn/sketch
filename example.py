import asyncio

from sketch import Application, Response, run_app

loop = asyncio.get_event_loop()


async def handler(request):
    username = request.match_info["username"]
    return Response(f"Hello, {username}")

app = Application(loop)

app.router.add_route("GET", "/{username}", handler)

if __name__ == "__main__":
    run_app(app, port=8080)
