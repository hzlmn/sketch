class HttpParserMixin:
    def on_body(self, data):
        self._body = data

    def on_url(self, url):
        self._url = url

    def on_message_complete(self):
        self._request = self._request_class(
            version=self._request_parser.get_http_version(),
            method=self._request_parser.get_method(),
            url=self._url,
            headers=self._headers,
            body=self._body,
            app=self._app,
        )

        self._request_handler_task = self._loop.create_task(
            self._request_handler(self._request, self.response_writer)
        )

    def on_header(self, header, value):
        header = header.decode(self._encoding)
        self._headers[header] = value.decode(self._encoding)
