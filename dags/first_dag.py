from airflow import DAG 
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    "owner" : "alphacpc",
    "retries" : 5,
    "retry_delay" : timedelta(minutes=2)
}

with DAG(
    dag_id="first_dag_v1",
    description="Mon Premier DAG",
    start_date=datetime(2022,8,3),
    schedule_interval='@daily'
) as dag:
    task1 = BashOperator(
        task_id='first_task',
        bash_command="echo hello worl, c'est ma premiere tache avec Airflow"
    )

    task2 = BashOperator(
        task_id='second_task',
        bash_command="echo hello worl, c'est mon deuxieme tache avec Airflow"
    )

    task1 >> task2