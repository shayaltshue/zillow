from acquire import acquire_data

import numpy as np
import pandas as pd

def drop_columns(df):
    df.drop(columns=['Unnamed: 0','fips', 'FIPS'], inplace=True)
    return df

def rename_columns(df):
    df.rename(columns={'bedroomcnt':'bedroom_count', 'bathroomcnt':'bathroom_count', 'calculatedfinishedsquarefeet':'total_sqft',
       'taxvaluedollarcnt':'tax_amount', 'Name':'county', 'State':'state'}, inplace=True)
    return df

def clean_data(df):
    df.replace(0, np.nan, inplace=True)
    df.dropna(inplace=True)
    
def wrangle_data(df):
    df = drop_columns(df)
    df = rename_columns(df)
    df = clean_data(df)
    print('Data Prepared')
    return df