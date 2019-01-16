import traceback

from .response import Response

server_exception_templ = """
<div>
    <h1>500 Internal server error</h1>
    <span>Server got itself in trouble : <b>{exc}</b><span>
    <p>{traceback}</p>
</div>
"""


def format_exception(exc):
    resp = Response(status=500, content_type="text/html")
    trace = traceback.format_exc().replace("\n", "</br>")
    msg = server_exception_templ.format(exc=str(exc), traceback=trace)
    resp.add_body(msg)
    return resp
