from bs4 import BeautifulSoup

import requests
import wget
import os
import shutil


class Scraper:

    def __init__(self):
        self.soup = BeautifulSoup(requests.get(
            'http://www.football-data.co.uk/englandm.php').text, "lxml")

    def scrape(self):
        dirName = 'epl_csvs'

        if os.path.exists(dirName):
            shutil.rmtree(dirName)

        os.makedirs(dirName)

        i = 0
        for link in self.soup.find_all('a', href=True, text='Premier League'):
            wget.download('http://www.football-data.co.uk/' + link.get('href'), dirName+'/'+str(i)+'_'+'EPL.csv')
            i = i + 1
