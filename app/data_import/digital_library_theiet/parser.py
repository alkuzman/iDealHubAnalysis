from bs4 import BeautifulSoup

from app.data_import.web_page_reader import WebPageReader


class DigitalLibraryParser(object):
    def __init__(self):
        self.web_page_reader = WebPageReader("digital-library.theiet.org")

    def spider(self, url):
        page = self.web_page_reader.read_from_url(url)
        print(page)
        soup = BeautifulSoup(page, 'html.parser')
        paginator = soup.find_all(class_="paginator")
        print(paginator)
