import pandas as pd

class ML:

    def __init__(self):
        self.df = pd.read_csv('epl_csvs/concacted.csv', engine='python', error_bad_lines=False)

    def pipeline(self):
        # rename columns
        self.df = cleanup_column_names(self.df, {})
        self.__wrangling()
    
    def __wrangling(self):
        print(123)
    
    def __visualization(self):
        pass
    
    def __featureEngineering(self):
        pass

    def __featureScaling(self):
        pass

    def __featureSelection(self):
        pass

    def __modeling(self):
        pass
    
    def __modelEvaluation(self):
        pass
    
    def __modelTuning(self):
        pass

    def __modelInterpretation(self):
        pass

    def __modelDeployment(self):
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