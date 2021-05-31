import requests
from bs4 import BeautifulSoup

def get_citation_needed_count(URL):
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')
    citation = soup.find_all('sup', class_="noprint Inline-Template Template-Fact")

    return len(citation)

def get_citations_needed_report(URL):
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')
    citation = soup.find_all('sup', class_="noprint Inline-Template Template-Fact")
    li = []
    counter = 0
    for i  in citation:
        if counter == 0:
            li.append(i.parent.text)
            counter = 1
        else:
            if i.parent.text in li:
                continue
            else:
                li.append(i.parent.text)
                counter = counter + 1
    string = '\n'.join(li)
    return string

print(get_citations_needed_report('https://en.wikipedia.org/wiki/History_of_Mexico'))