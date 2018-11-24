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

            "b365h": "bet365_home_win_odds",
            "b365d": "bet365_draw_odds",
            "b365a": "bet365_away_win_odds",

            "bsh": "blue_square_home_win_odds",
            "bsd": "blue_square_draw_odds",
            "bsa": "blue_square_away_win_odds",
            "bwh": "bet_win_home_win_odds",
            "bwd": "bet_win_draw_odds",
            "bwa": "bet_win_away_win_odds",
            "gbh": "gamebookers_home_win_odds",
            "gbd": "gamebookers_draw_odds",
            "gba": "gamebookers_away_win_odds",
            "iwh": "interwetten_home_win_odds",
            "iwd": "interwetten_draw_odds",
            "iwa": "interwetten_away_win_odds",
            "lbh": "ladbrokes_home_win_odds",
            "lbd": "ladbrokes_draw_odds",
            "lba": "ladbrokes_away_win_odds",

            "psh" : "pinnacle_home_win_odds",
            "psa" : "pinnacle_away_win_odds",
            "psd" : "pinnacle_draw_odds",
            "pd" : "pinnacle_draw_odds",
            "ph" : "pinnacle_home_win_odds",
            "pa" : "pinnacle_away_win_odds",

            "soh": "sporting_odds_home_win_odds",
            "sod": "sporting_odds_draw_odds",
            "soa": "sporting_odds_away_win_odds",
            "sbh": "sportingbet_home_win_odds",
            "sbd": "sportingbet_draw_odds",
            "sba": "sportingbet_away_win_odds",
            "sjh": "stan_james_home_win_odds",
            "sjd": "stan_james_draw_odds",
            "sja": "stan_james_away_win_odds",
            "syh": "stanleybet_home_win_odds",
            "syd": "stanleybet_draw_odds",
            "sya": "stanleybet_away_win_odds",
            "vch": "vc_bet_home_win_odds",
            "vcd": "vc_bet_draw_odds",
            "vca": "vc_bet_away_win_odds",
            "whh": "william_hill_home_win_odds",
            "whd": "william_hill_draw_odds",
            "wha": "william_hill_away_win_odds",

            "bb1x2": "bet_brain_bookmakers_count_odds",
            "bbmxh": "betbrain_maximum_home_win_odds",
            "bbavh": "betbrain_average_home_win_odds",
            "bbmxd": "betbrain_maximum_draw_odds",
            "bbavd": "betbrain_average_draw_win_odds",
            "bbmxa": "betbrain_maximum_away_win_odds",
            "bbava": "betbrain_average_away_win_odds",

            "maxh": "oddsportal_maximum_home_win_odds",
            "maxd": "oddsportal_maximum_draw_win_odds",
            "maxa": "oddsportal_maximum_away_win_odds",
            "avgh": "oddsportal_average_home_win_odds",
            "avgd": "oddsportal_average_draw_win_odds",
            "avga": "oddsportal_average_away_win_odds",
            "bbou": "bet_brain_bookmakers_count_over_under",

            "bbmx>2.5": "betbrain_maximum_over_2_5_goals",
            "bbav>2.5": "betbrain_average_over_2_5_goals",
            "bbmx<2.5": "betbrain_maximum_under_2_5_goals",
            "bbav<2.5": "betbrain_average_under_2_5_goals",

            "gb>2.5": "gamebookers_over_2_5_goals",
            "gb<2.5": "gamebookers_under_2_5_goals",

            "b365>2.5": "bet365_over_2_5_goals",
            "b365<2.5": "bet365_under_2_5_goals",

            "bbah": "bet_brain_bookmakers_count_used_handicap",
            "bbahh": "betbrain_size_of_handicap_home_team",

            "bbmxahh": "betbrain_maximum_asian_handicap_home_team_odds",
            "bbavahh": "betbrain_average_asian_handicap_home_team_odds",
            "bbmxaha": "betbrain_maximum_asian_handicap_away_team_odds",
            "bbavaha": "betbrain_average_asian_handicap_away_team_odds",
            "b365ahh": "bet365_asian_handicap_home_team_odds",
            "b365aha": "bet365_asian_handicap_away_team_odds",
            "b365ah": "bet365_size_of_handicap_home_team",

            "gbah": "gamebookers_size_of_handicap_home_team",
            "lbah": "ladbrokes_size_of_handicap_home_team",

            "lbahh": "ladbrokes_asian_handicap_home_team_odds",
            "lbaha": "ladbrokes_asian_handicap_away_team_odds",
            "gbahh": "gamebookers_asian_handicap_home_team_odds",
            "gbaha": "gamebookers_asian_handicap_away_team_odds",

            "psch": "pinnacle_closing_home_win",
            "pscd": "pinnacle_closing_draw",
            "psca": "pinnacle_closing_away_win",

        }

        df.rename(index=str, columns=columnsMap, inplace=True)
        df.to_csv(self.csvDir+'/concacted.csv', index=False)
