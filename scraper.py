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
            df = pd.read_csv(path, engine='python', error_bad_lines=False)
            dfLower = df.apply(lambda x: x.astype(str).str.lower())
            dfLower.columns = map(str.lower, dfLower.columns)
            dfLower.to_csv(path, index=False)
            if (len(dfLower.columns) < 40):
                os.remove(path)

    def concactCSVs(self):
        if os.path.exists(self.csvDir+'/concacted.csv'):
            os.remove(self.csvDir+'/concacted.csv')
        df = None
        for path in glob.glob(self.csvDir+'/*.csv'):
            if df is None:
                df = pd.read_csv(path, engine='python', error_bad_lines=False)
            else:
                tmpDF = pd.read_csv(path, engine='python',
                                    error_bad_lines=False)
                df = pd.concat([df, tmpDF], ignore_index=True)

        # rename columns
        columnsMap = {
            "abp": "away_team_bookings_points",
            "ac": "away_team_corners",
            "af": "away_team_fouls_committed",
            "fthg": "full_time_home_team_goals",
            "hg": "home_team_goals",
            "ftag": "full_time_away_team_goals",
            "ag": "away_team_goals",
            "ftr": "full_time_result",
            "hthg": "half_time_home_team_goals",
            "htag": "half_time_away_team_goals",
            "htr": "half_time_result",
            "attendance": "crowd_attendance",
            "referee": "match_referee",
            "hs": "home_team_shots",
            "as": "away_team_shots",
            "hst": "home_team_shots_on_target",
            "ast": "away_team_shots_on_target",
            "hhw": "home_team_hit_woodwork",
            "ahw": "away_team_hit_woodwork",
            "hbp": "home_team_bookings_points_10_yellow_25_red",
            "abp": "away_team_bookings_points_10_yellow_25_red",
            "hfkc": "home_team_free_kicks_conceded",
            "afkc": "away_team_free_kicks_conceded",
            "hc": "home_team_corners",
            "ac": "away_team_corners",
            "hf": "home_team_fouls_committed",
            "af": "away_team_fouls_committed",
            "ho": "home_team_offsides",
            "ao": "away_team_offsides",
            "hy": "home_team_yellow_cards",
            "ay": "away_team_yellow_cards",
            "hr": "home_team_red_cards",
            "ar": "away_team_red_cards",
        }
        df.rename(index=str, columns=columnsMap, inplace=True)
        df.to_csv(self.csvDir+'/concacted.csv', index=False)
