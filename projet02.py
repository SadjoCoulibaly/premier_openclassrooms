import requests
from bs4 import BeautifulSoup
import csv

url = 'http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'
resultat = requests.get(url)
liste = []
liste1 = []
if resultat.ok:
    soup = BeautifulSoup(resultat.text, 'lxml')

    data = soup.find_all('th', text='')
    liste.append(data)
    data2 = soup.find_all('td', text='')
    liste1.append(data2)

    for i in liste:
        print(i)
        for j in liste1:
            print(j)

    """data = soup.find_all('th')
    for i in data:
        print(i.string)

    data1 = soup.find_all('td')
    for j in data1:
        print(j.string)"""



