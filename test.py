import requests
from bs4 import BeautifulSoup


def url_donnee(url_lien):
    global soup
    result_url = requests.get(url_lien)
    if result_url.ok:
        soup = BeautifulSoup(result_url.text, 'lxml')
        d1 = soup.find('h1')
        print(d1.text)
    return url_lien, soup


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
    print(tab)
    return tab


d1 = donnee('th')

d2 = donnee('td')
