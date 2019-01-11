<div align="center">
  <p>:warning: Work in progress</p>
  <h3>Sketch</h3>
  <p>Super tiny <a href="https://github.com/aio-libs/aiohttp">aiohttp</a> clone, made for upcoming <a href="">DIY Async Web Framework</a> guide</p>
  <a href="https://github.com/ambv/black"><img alt="Code style: black" src="https://camo.githubusercontent.com/28a51fe3a2c05048d8ca8ecd039d6b1619037326/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f636f64652532307374796c652d626c61636b2d3030303030302e737667" data-canonical-src="https://img.shields.io/badge/code%20style-black-000000.svg" style="max-width:100%;"></a>
</div>

### Features :sparkles:
- Application container
- Lifecycle hooks
- Middlewares
- Routing
- Request/Response helpers
- ...

### Overview

To give you a first grasp, here is simple example of app made with `sketch`

`app.py`
```python3
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

```

```shell
$ python app.py
>> Started server on 127.0.0.1:8080
```

```shell
$ curl http://127.0.0.1:8080/oleh                                               
>> Hello, oleh
```

### License
MIT
