import pandas as pd
import numpy as np

def transform_altitude(df:pd.DataFrame)-> pd.DataFrame:
    df["altitude_mean_log"] = np.log(df["altitude_mean_meters"])
    df = df.drop(['altitude_mean_meters', ], axis=1)
    return df
    

#'Unnamed: 0' and Quakers
def drop_column(df:pd.DataFrame, col_name: str) -> pd.DataFrame:
    df = df.drop([col_name], axis=1)
    return df

def fill_missing_values(df:pd.DataFrame) -> pd.DataFrame:
    altitude_low_meters_mean=1500.3684210526317
    altitude_high_meters_mean=1505.6315789473683
    altitude_mean_log_mean=7.0571530664031155
    df["altitude_low_meters"] = df["altitude_low_meters"].fillna(altitude_low_meters_mean)
    df["altitude_high_meters"] = df["altitude_high_meters"].fillna(altitude_high_meters_mean)
    df["altitude_mean_log"] = df["altitude_mean_log"].fillna(altitude_mean_log_mean)
    return df

def check_for_zero_values(df:pd.Dataframe) -> pd.DataFrame:
    df_pp = df.copy()
    missing = pd.DataFrame((df_pp==0).sum(), columns=["Zero_Amount"])
    missing.head()
    missing['Percentage'] = round((missing['Zero_Amount']/df.shape[0])*100, 2)
    missing[missing['Zero_Amount'] != 0].sort_values(by = 'Percentage', ascending=False)
    return missing