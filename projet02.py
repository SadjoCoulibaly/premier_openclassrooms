import requests
from bs4 import BeautifulSoup
import csv

url = 'http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'
resultat = requests.get(url)
"""liste = []
liste1 = []"""

if resultat.ok:
    soup = BeautifulSoup(resultat.text, 'lxml')

    data = soup.find_all('th')

    data1 = soup.find_all('td')

    with open('donnee.csv', 'w') as f:
        writer = csv.writer(f)
        for row in data:
            writer.writerow(row)
        for column in data1:
            writer.writerow(column)

    """for i in data:
        liste.append(i)
        while i != len(liste):
            print(liste)"""

    """data2 = soup.find_all('td', text='')
    liste1.append(data2)
    t = len(liste1)
    print(t)
    for i in liste:
        print(i)
        for j in liste1:
            print(j)
    i = 0
    j = 0
    while i in len(liste):
        while j in len(liste1):
            print(liste[i], ':', liste1[j])"""

    """data = soup.find_all('th')
    for i in data:
        print(i.string)

    data1 = soup.find_all('td')
    for j in data1:
        print(j.string)"""
