
from datetime import datetime
from datetime import timedelta

from airflow.decorators import dag, task
from pendulum import today

import sys

sys.path.insert(0, '/opt/process_functions')

from connect_api import get_prediction_document


@dag(
    dag_id="predict_data",
    description="Predict data from a file to another DAG",
    tags=["detection files"],
    default_args={'owner': 'airflow'},
    schedule_interval=timedelta(minutes=2),
    start_date=today().add(hours=-1)
)


def ingest_data():

    @task
    def get_data_ingest_from_local_file_task():
        return _get_data_ingest_from_local_file()

    @task
    def save_data(data_to_ingest_df):
        _save_data(data_to_ingest_df)

    # Task relationships
    data_to_ingest = get_data_ingest_from_local_file_task()
    save_data(data_to_ingest)


ingest_data_dag = ingest_data()


def _get_data_ingest_from_local_file():
    import pandas as pd
    input_data_df = pd.read_csv("/opt/airflow/input_data/stroke_data.csv")
    data_ingest_df = input_data_df.sample(n=5)

    return data_ingest_df.to_json(orient="index")


def _save_data(data_ingest_js):
    import pandas as pd
    data_ingest_df = pd.read_json(data_ingest_js, orient='index')

    filepath = f"/opt/airflow/output_data/{datetime.now()}.csv"

    data_ingest_df = get_prediction_document(filepath, data_ingest_df)
    data_ingest_df.to_csv(filepath, index=False)
