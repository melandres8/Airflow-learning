from airflow.models import DAG
from airflow.providers.sqlite.operators.sqlite import SqliteOperator

from datetime import datetime

default_args = {
    'start_date': datetime(2022, 4, 24)
}

with DAG('user_processing', schedule_interval='@daily',
    default_args=default_args,
    catchup=False) as dag:
    #Define tasks/operators

    creating_table = SqliteOperator(
        task_id='creating_table',
        sqlite_conn_id='db_sqlite',
        sql='''
            CREATE TABLE users (
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                country TEXT NOT NULL,
                username TEXT NOT NULL,
                password TEXT NOT NULL,
                email TEXT NOT NULL PRIMARY KEY
            );
        '''
    )
