import pandas as pd
from terminaltables import AsciiTable


class ML:

    def __init__(self):
        self.df = pd.read_csv('epl_csvs/concacted.csv',
                              engine='python', error_bad_lines=False)

    def pipeline(self):
        # rename columns
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
            columns_table_rows.append([c, self.df.dtypes[c].name, df_length - self.df[c].count()])
        columns_table = AsciiTable(columns_table_rows)

    def __wrangling(self):
        pass
    
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

def cleanup_column_names(df,rename_dict={},do_inplace=True):
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
        return df.rename(columns={col: col.lower().replace(' ','_')
                    for col in df.columns.values.tolist()},
                  inplace=do_inplace)
    else:
        return df.rename(columns=rename_dict,inplace=do_inplace)
