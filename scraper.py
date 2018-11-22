from bs4 import BeautifulSoup

import requests


class Scraper:

    def __init__(self):
        self.soup = BeautifulSoup(requests.get('http://www.football-data.co.uk/englandm.php').text, "lxml")

    def scrape(self):
        for link in self.soup.find_all('a', href=True, text='Premier League'):
            print(link.get('href'))
