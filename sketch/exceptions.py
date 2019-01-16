import traceback

from .response import Response


class HTTPException(Response, Exception):
    status_code = None

    def __init__(self, reason=None, content_type=None):
        self._reason = reason
        self._content_type = content_type

        Response.__init__(
            self,
            body=self._reason,
            status=self.status_code,
            content_type=self._content_type or "text/plain",
        )

        Exception.__init__(self, self._reason)


class HTTPNotFound(HTTPException):
    status_code = 404


class HTTPBadRequest(HTTPException):
    status_code = 400


class HTTPFound(HTTPException):
    status_code = 302

    def __init__(self, location, reason=None, content_type=None):
        super().__init__(reason=reason, content_type=content_type)
        self.add_header("Location", location)
