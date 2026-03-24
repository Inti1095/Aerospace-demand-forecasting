import pandas as pd

def create_time_features(df, date_col):
    df[date_col] = pd.to_datetime(df[date_col])
    df["year"] = df[date_col].dt.year
    df["month"] = df[date_col].dt.month
    df["day"] = df[date_col].dt.day
    return df

def create_lag_features(df, target_col, lags=[1, 2, 3]):
    for lag in lags:
        df[f"{target_col}_lag_{lag}"] = df[target_col].shift(lag)
    return df

def create_rolling_features(df, target_col, windows=[3, 7]):
    for window in windows:
        df[f"{target_col}_rolling_mean_{window}"] = (
            df[target_col].rolling(window=window).mean()
        )
    return df
