import requests
from bs4 import BeautifulSoup
import json

def GetInfoFromWiki(url):
    result = {}
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        information = soup.find_all()
        text = ""
        for info in information:
            if info.name == 'div':
                info_class = info.attrs.get('class')
                if info_class:
                    info_class = " ".join(info_class)
                    if info_class in ["mw-heading mw-heading2", "mw-heading mw-heading3"]:
                        break

            if info.name == "p":
                text += info.get_text() + " "

    result['Overview'] = text.strip()

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        heading_div = ["mw-heading mw-heading2", "mw-heading mw-heading3"]
        headings = soup.find_all(class_=heading_div)
        for heading in headings:
            heading_class = " ".join(heading.attrs.get('class'))
            heading_text = heading.get_text(strip=True)
            next_sibling = heading.find_next_sibling()
            text = ""
            while next_sibling:
                if next_sibling.name == 'div':
                    next_sibling_class = " ".join(next_sibling.attrs.get('class'))
                    if next_sibling_class in heading_div:
                        break
                if next_sibling.name == 'p':
                    text += next_sibling.get_text() + " "
                next_sibling = next_sibling.find_next_sibling()

            if text:
                result[heading_text] = text.strip()

    print("Information extracted from Wikipedia")
    return result