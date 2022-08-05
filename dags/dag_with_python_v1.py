from datetime import timedelta, datetime
from airflow import DAG
from airflow.operators.python import PythonOperator

default_args = {
    'owner' : 'alphacpc',
    'retries' : 2,
    'retry_delay': timedelta(minutes=0.1)
}

def greet():
    print("Hello Mafé !!!")

with DAG(
    default_args=default_args,
    dag_id="first_dag_python_operator_v1",
    description="Mon premier DAG python",
    start_date=datetime(2022, 8,3),
    schedule_interval="@daily"
) as dag:
    task1 = PythonOperator(
        task_id="greet",
        python_callable=greet 
    )

    task1