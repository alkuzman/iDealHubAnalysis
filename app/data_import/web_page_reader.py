import http.client


class WebPageReader(object):

    def __init__(self, host):
        self.connection = http.client.HTTPConnection(host, timeout=2)

    def read_from_url(self, url):
        self.connection.request('GET', url)
        response = self.connection.getresponse()
        content = response.read().decode('utf-8')

        return content
