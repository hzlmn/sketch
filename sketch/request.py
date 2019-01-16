from yarl import URL


class Request:
    def __init__(self, method, url, headers, version=None, body=None, app=None):
        self._version = version
        self._encoding = "utf-8"
        self._method = method.decode(self._encoding)
        self._url = URL(url.decode(self._encoding))
        self._headers = headers
        self._body = body
        self._app = app
        self._match_info = {}

    @property
    def app(self):
        return self._app

    @property
    def match_info(self):
        return self._match_info

    @match_info.setter
    def match_info(self, match_info):
        self._match_info = match_info

    @property
    def method(self):
        return self._method

    @property
    def url(self):
        return self._url

    @property
    def headers(self):
        return self._headers

    def text(self):
        if self._body is not None:
            return self._body.decode(self._encoding)

    def json(self):
        text = self.text()
        if text is not None:
            return json.loads(text)

    def __repr__(self):
        return f"<Request at 0x{id(self)}>"
