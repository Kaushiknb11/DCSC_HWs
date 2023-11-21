from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from Scripts.etl import extract_data, transform_data, load_data
from datetime import datetime, timedelta
import pandas as pd
import requests
import boto3
import requests
import io
import time
import logging
from sqlalchemy import create_engine

import sys
from dotenv import load_dotenv
import os
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning) 


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 11, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}


dag = DAG('shelter_data_dag',
          default_args=default_args,
          description='DAG for Animal Shelter Data',
          schedule_interval=timedelta(days=1))


extract_data_task = PythonOperator(
    task_id='extract_data',
    python_callable=extract_data,
    dag=dag)



transform_data_task = PythonOperator(
    task_id='transform_data',
    python_callable=transform_data,
    dag=dag)


load_data_task = PythonOperator(
    task_id='load_data',
    python_callable=load_data,
    dag=dag)



extract_data_task >> transform_data_task >> load_data_task


