import pandas as pd
import numpy as np
import sys

def extract_data(source):
    return pd.read_csv(source)

def transform_data(data):
    new_data=data.copy()
    new_data.rename(columns={'Unnamed: 0': 'IDs'}, inplace=True)
    new_data.dropna(inplace=True)
    new_data.drop(columns=['Weight'], inplace=True)
    new_data['Ram'] = new_data['Ram'].str.replace('GB', '')
    return new_data

def load_data(data, destination):
    data.to_csv(destination)

if __name__ == "__main__":
    arg = sys.argv
    print("Starting....")
    df = extract_data(arg[1])
    new_df = transform_data(df)
    load_data(new_df, arg[2])
    print("Complete")































