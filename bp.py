import requests
from bs4 import BeautifulSoup





class BookParser():
    def __init__(self):
        self.books = []
        self.series = []
        self.authors = []

    def sort_long_text(full_tag):
        text = full_tag.text
        list_text = full_tag.text.split(sep=" ")
        lenght = len(list_text)
        count = list_text[lenght - 2] + " " + list_text[lenght - 1]
        index = (text.find(count))
        name = (text[:index])
        return count, name
    def find_links(self, ask):
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
                count, name = sort_long_text(full_tag)
                print(name,count)
                self.series.append(Collection(link, name, count))

            case 'b':
                text = full_tag.text.split(sep=" - ")
                if len(text) != 2:
                    return
                name = text[0]
                author = text[1]
                self.books.append(Book(link, name, author))

            case "a":
                text = full_tag.text
                if text == "Авторы":
                    return
                count, name = sort_long_text(full_tag)
                print(name,count)

                self.authors.append(Collection(link, name, count))

            case _:
                pass


class Book:
    def __init__(self, link, name, author):
        self.link = link
        self.name = name
        self.author = author


class Collection:
    def __init__(self, link, name, count):
        self.link = link
        self.name = name
        self.count = count


myParser = BookParser()