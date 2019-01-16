import re
from functools import partialmethod

from .exceptions import HTTPNotFound


class UrlDispatcher:
    _param_regex = r"{(?P<param>\w+)}"

    def __init__(self):
        self._routes = {}

    def resolve(self, request):
        for (method, pattern), handler in self._routes.items():
            match = re.match(pattern, request.url.raw_path)

            if match is None:
                raise HTTPNotFound(reason=f"Could not find {request.url.raw_path}")

            if method != request.method:
                raise HTTPNotFound(
                    reason=f"{request.method} not allowed for {request.url.raw_path}"
                )

            return match.groupdict(), handler

    def _format_pattern(self, path):
        regex = r""
        last_pos = 0

        for match in re.finditer(self._param_regex, path):
            regex += path[last_pos: match.start()]
            param = match.group("param")
            regex += r"(?P<%s>\w+)" % param
            last_pos = match.end()

        return regex

    def add_route(self, method, path, handler):
        pattern = self._format_pattern(path)
        self._routes[(method, pattern)] = handler

    add_get = partialmethod(add_route, "GET")

    add_post = partialmethod(add_route, "POST")

    add_put = partialmethod(add_route, "PUT")

    add_head = partialmethod(add_route, "HEAD")

    add_options = partialmethod(add_route, "OPTIONS")
