# data related dependencies 
import pandas as pd
import psycopg2
from sqlalchemy import create_engine
import sys

def extract(url):
    
    # https://data.austintexas.gov/resource/9t4d-g238.json
    data = pd.read_json(url)
    
    print("Input data received")
    print('='*10)
    return data


def transform(data):

    print('Transforming the Data')
    data.fillna('Not Recorded',inplace=True)
    data['outcome_type_id'] = data.index + 1
    data['outcome_event_id'] = data.index + 1

    # Dividing into entities 
    animal_table = ['animal_id', 'breed', 'color', 'name','date_of_birth','animal_type']
    outcome_table = ['outcome_type_id','outcome_type']
    outcome_event = ['outcome_event_id','datetime','sex_upon_outcome','outcome_subtype','animal_id','outcome_type']
    data_colums_order = ['animal_id',
            'outcome_type','outcome_event_id']

    # re-ordering
    animal = data[animal_table]
    outcomes = data[outcome_table]
    outcome_events = data[outcome_event]
    data = data[data_colums_order]
   
    # Correcting Duplication
    animal.drop_duplicates(inplace=True)
    outcomes = pd.DataFrame(pd.Series(outcomes['outcome_type'].unique(),name='outcome_type'))
    outcomes['outcome_type_id'] = outcomes.index + 1 
    outcomes = outcomes[['outcome_type_id','outcome_type']]
    outcomes_2 = outcomes[['outcome_type','outcome_type_id']]
    
    #mapping outcome_type_id values in the outcome_events table
    dictionary_of_outcomes = dict(zip(outcomes_2['outcome_type'],outcomes_2['outcome_type_id']))
    outcome_events['outcome_type_id']= outcome_events['outcome_type'].map(dictionary_of_outcomes)


    outcome_events = outcome_events.drop('outcome_type', axis=1)

    data["outcome_type_id"] = data['outcome_type'].map(dictionary_of_outcomes)
    data = data.drop('outcome_type', axis=1)


    print('Data transformation completed')
    print('='*10)

    return data, animal, outcomes, outcome_events
    


def load(transformed_data: list):
    
    print('Received transformed data.')
    fact_table, animal, outcomes, outcome_events = transformed_data
    print('='*10)
    print('Starting up Postgres')
    print('Postgres connection successful')
    
    DATABASE_URL = "postgresql+psycopg2://kaushik:test123@db:5432/shelter"
    engine = create_engine(DATABASE_URL)

    animal.to_sql('animal', engine, if_exists='append', index=False)
    outcomes.to_sql('outcome_type', engine, if_exists='append', index=False)
    outcome_events.to_sql('outcome_event', engine, if_exists='append', index=False)
    fact_table.to_sql('fact_table', engine, if_exists='append', index=False)

    print('Loading Data')
    print('='*10)
    print('Completed Data Loading!')



if __name__ == '__main__':

    # Data Source 
    args = sys.argv
    data_url = args[1]

    # etl_obj
    data = extract(url=data_url)

    transformed_data = transform(data) # returns transformed 
    



    load(transformed_data) # takes transformed data