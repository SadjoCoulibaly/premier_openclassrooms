import requests
from bs4 import BeautifulSoup


def url_donnee(url_lien):
    global soup
    result_url = requests.get(url_lien)
    if result_url.ok:
        soup = BeautifulSoup(result_url.text, 'lxml')

    return url_lien, soup


def le_titre(title=''):
    lien = 'http://books.toscrape.com/catalogue/worlds-elsewhere-journeys-around-shakespeares-globe_972/index.html'
    url_donnee(lien)
    d = soup.find(title)
    print(d.text)
    return d


def recuperation(rec=''):
    lien = 'http://books.toscrape.com/catalogue/worlds-elsewhere-journeys-around-shakespeares-globe_972/index.html'
    url_donnee(lien)
    data = soup.find_all(rec)
    return data


def donnee(bal=''):
    iii = recuperation(bal)
    tab = []
    for i in iii:
        tab.append(i.string)
    return tab


t = le_titre('h1')
d1 = donnee('th')
d2 = donnee('td')

glo = dict(zip(d1, d2))
print(glo)
