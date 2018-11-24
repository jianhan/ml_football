from bs4 import BeautifulSoup

import requests
import wget
import os
import shutil
import pandas as pd
import glob

class Scraper:

    def __init__(self):
        self.csvDir = 'epl_csvs'
        self.host = 'http://www.football-data.co.uk/'
        self.soup = BeautifulSoup(requests.get(
            self.host+'englandm.php').text, "lxml")

    def scrape(self):
        if os.path.exists(self.csvDir):
            shutil.rmtree(self.csvDir)

        os.makedirs(self.csvDir)

        i = 0
        for link in self.soup.find_all('a', href=True, text='Premier League'):
            wget.download(self.host +
                          link.get('href'), self.csvDir+'/'+str(i)+'_'+'EPL.csv')
            i = i + 1
    
    def combineCSVs(self):
        for path in glob.glob(self.csvDir+'/*.csv'):
            print(path)
            df = pd.read_csv(path, engine='python', error_bad_lines=False)
            dfLower = df.apply(lambda x: x.astype(str).str.lower())
            dfLower.columns = map(str.lower, dfLower.columns)
            dfLower.to_csv(path, index=False)
            print('SUCCESSFUL')