import requests
from bs4 import BeautifulSoup
import csv

url = 'http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'
resultat = requests.get(url)
liste = {}
if resultat.ok:
    soup = BeautifulSoup(resultat.text, 'lxml')
    titre = soup.find('h1')

    data = soup.find_all('th')
    for i in data:
        l1 = [liste.append(i.string)]

    data1 = soup.find_all('td')
    for j in data1:
        l2 = [liste.append(j.string)]

liste = {l1: l2}
print(liste)
