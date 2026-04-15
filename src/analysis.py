import pandas as pd  

def load_data(path):
    return pd.read_csv(path)

def clean_data(df):
    df = df.dropna()
    return df

def vote_percentage(df):
    return (df['choice'].value_counts(normalize=True) * 100).round(2)

def region_analysis(df):
    return pd.crosstab(df['region'], df['choice'])

def age_analysis(df):
    return pd.crosstab(df['age_group'], df['choice'])

def trend_analysis(df):
    df['date'] = pd.to_datetime(df['date'])
    trend = df.groupby(['date', 'choice']).size().unstack().fillna(0)
    return trend