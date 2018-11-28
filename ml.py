import pandas as pd
from terminaltables import AsciiTable


class ML:

    def __init__(self):
        self.df = pd.read_csv('epl_csvs/concacted.csv',
                              engine='python', error_bad_lines=False)

    def pipeline(self):
        # rename columns
        self.__wrangling()
        self.__description()

    def __description(self):
        df_length = len(self.df)

        # table summary
        summary_table_data = [
            ['rows', 'columns'],
            [self.df.shape[0], self.df.shape[1]],
        ]
        summary_table = AsciiTable(summary_table_data)
        print(summary_table.table)

        # columns summary
        columns_table_rows = [['column', 'type', 'missing values']]
        for c in self.df.columns.values:
            columns_table_rows.append(
                [c, self.df.dtypes[c].name, df_length - self.df[c].count()])

        columns_table = AsciiTable(columns_table_rows)
        print(columns_table.table)

    def __wrangling(self):
        df_length = len(self.df)
        # manually drop columns we do not need
        self.df.drop(
            [
                'stan_james_away_win_odds',
                'stan_james_draw_odds',
                'stan_james_home_win_odds',

                'sportingbet_away_win_odds',
                'sportingbet_draw_odds',
                'sportingbet_home_win_odds',

                'gamebookers_away_win_odds',
                'gamebookers_draw_odds',
                'gamebookers_home_win_odds',

                'vc_bet_away_win_odds',
                'vc_bet_draw_odds',
                'vc_bet_home_win_odds',

                'bet_win_away_win_odds',
                'bet_win_draw_odds',
                'bet_win_home_win_odds',

                'away_team_corners',
                'away_team_fouls_committed',
                'away_team_red_cards',
                'away_team_shots',
                'away_team_shots_on_target',
                'away_team_yellow_cards',
                'full_time_away_team_goals',
                'full_time_home_team_goals',
                'home_team_corners',
                'home_team_fouls_committed',
                'home_team_red_cards',
                'home_team_shots',
                'home_team_shots_on_target',
                'half_time_away_team_goals',
                'half_time_home_team_goals',
                'half_time_result',
                'home_team_yellow_cards'
            ],
            axis=1,
            inplace=True)

        # drop any column with missing data more than 50%
        for c in self.df.columns.values:
            if df_length - self.df[c].count() > 0.25 * df_length:
                # if the number of missing value is over 25%, then there is no point to leave
                # this column in dataset
                self.df.drop([c], axis=1, inplace=True)
    
        # type casting
        self.df['date'] = pd.to_datetime(self.df.date)
        self.df.dropna(inplace=True)

    def __visualization(self):
        pass

    def __feature_engineering(self):
        pass

    def __feature_scaling(self):
        pass

    def __feature_selection(self):
        pass

    def __modeling(self):
        pass

    def __model_evaluation(self):
        pass

    def __modelTuning(self):
        pass

    def __model_interpretation(self):
        pass

    def __model_deployment(self):
        pass


def cleanup_column_names(df, rename_dict={}, do_inplace=True):
    """This function renames columns of a pandas dataframe
       It converts column names to snake case if rename_dict is not passed.
    Args:
        rename_dict (dict): keys represent old column names and values point to
                            newer ones
        do_inplace (bool): flag to update existing dataframe or return a new one
    Returns:
        pandas dataframe if do_inplace is set to False, None otherwise
    """
    if not rename_dict:
        return df.rename(columns={col: col.lower().replace(' ', '_')
                                  for col in df.columns.values.tolist()},
                         inplace=do_inplace)
    else:
        return df.rename(columns=rename_dict, inplace=do_inplace)
