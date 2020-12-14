import requests
from bs4 import BeautifulSoup


url = 'http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'
resultat = requests.get(url)

if resultat.ok:
    soup = BeautifulSoup(resultat.text, 'lxml')
    titre = soup.find('h1')
    print(titre.text)
