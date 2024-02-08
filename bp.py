import requests
from bs4 import BeautifulSoup


def sort_link(full_tag, link):
    link_parts = link.split(sep="/")

    if len(link_parts) != 3:
        return
    link_type = link_parts[1]

    match link_type:
        case 'sequence':
            print(full_tag)
            print(link)
        case 'b':
            print(full_tag)
            print(link)
        case _:
            pass


def find_all_links(ask):
    request = requests.get(f"https://flibusta.site/booksearch?ask={ask}")
    soup = BeautifulSoup(request.text, "html.parser")

    for li_tag in soup.find_all('li'):
        a_tag = li_tag.find("a")
        href = a_tag.get("href") if a_tag else None
        sort_link(li_tag, href) if href else None


