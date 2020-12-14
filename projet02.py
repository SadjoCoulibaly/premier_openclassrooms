import requests
from bs4 import BeautifulSoup


url = 'http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'
resultat = requests.get(url)
list1 = []
if resultat.ok:
    soup = BeautifulSoup(resultat.text, 'lxml')
    titre = soup.find('h1')
    print(titre.text)
    data = soup.find_all('th')

    data1 = soup.find_all('td')

    for i in data:
        print(i.string)
    for j in data1:
        print(j.string)