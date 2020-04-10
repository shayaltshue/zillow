import env

import os.path
import pandas as pd

def data_already_acquired():
    return os.path.isfile('zillow.csv')
    
def get_sql_data():
    query = """
    SELECT  bedroomcnt, 
		bathroomcnt,
        calculatedfinishedsquarefeet,
		taxvaluedollarcnt,
        taxamount,
		fips
    FROM properties_2017 as p
    JOIN predictions_2017 as pr USING(`parcelid`)
    WHERE propertylandusetypeid = 261 and (transactiondate >= '2017-05-01' AND transactiondate <= '2017-06-31')
    """

    zillow_url = get_url_for_pancakes('zillow')
    zillow_df = pd.read_sql(query, zillow_url)
    return zillow_df


def get_fips():
    fips = pd.read_table('FIPS.txt')
    fips.head()
    return fips

def merge_data(zillow_df, fips_df):
    merged_df = pd.merge(left=zillow_df, right=fips_df, left_on='fips', right_on='FIPS')
    return merged_df

def generate_csv():
    if data_already_acquired():
        print('csv has been previously generated.')
    else:
        df = merge_data(get_sql_data(), get_fips())
        df.to_csv('zillow.csv')
        print('csv was generated')
    
def acquire_data():
    generate_csv()
    print('Data Acquired')
    return pd.read_csv('zillow.csv')
    