import requests
from bs4 import BeautifulSoup


def create_collection(full_tag, link):
    text = full_tag.text
    list_text = full_tag.text.split(sep=" ")

    lenght = len(list_text)
    count = list_text[lenght - 2] + " " + list_text[lenght - 1]
    name = (text[:text.find(count)])
    return Element(link, name, count)


class BookParser:
    def __init__(self):
        self.books = []
        self.series = []
        self.authors = []

    def parse_site(self, ask):
        request = requests.get(f"https://flibusta.site/booksearch?ask={ask}")
        soup = BeautifulSoup(request.text, "html.parser")

        for li_tag in soup.find_all('li'):
            a_tag = li_tag.find("a")
            href = a_tag.get("href") if a_tag else None
            self.compare_link(li_tag, href) if href else None

    def compare_link(self, full_tag, link):
        link_parts = link.split(sep="/")
        link_type = link_parts[1]

        match link_type:
            case 'sequence':
                self.series.append(create_collection(full_tag, link))

            case 'b':
                text = full_tag.text.split(sep=" - ")
                if len(text) != 2:
                    return

                name = text[0]
                author = text[1]
                self.books.append(Element(link, name, author))

            case "a":
                text = full_tag.text
                if text == "Авторы":
                    return
                self.authors.append(create_collection(full_tag, link))

            case _:
                pass


class Element:
    def __init__(self, link, name, extra):
        self.link = link
        self.name = name
        self.extra = extra


