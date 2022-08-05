from datetime import timedelta, datetime
from airflow import DAG
from airflow.operators.python import PythonOperator

default_args = {
    'owner' : 'alphacpc',
    'retries' : 2,
    'retry_delay': timedelta(minutes=0.1)
}

def greet(name, job):
    print(f"Je m'appelle {name}", f"et je suis {job}")

with DAG(
    default_args=default_args,
    dag_id="first_dag_python_operator_v2",
    description="Mon premier DAG python",
    start_date=datetime(2022, 8,3),
    schedule_interval="@daily"
) as dag:
    task1 = PythonOperator(
        task_id="greet_v2",
        python_callable=greet,
        op_kwargs={'name':'Alpha','job':'mafe'}
    )

    task1