from airflow import DAG 
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    "owner" : "alphacpc",
    "retries" : 5,
    "retry_delay" : timedelta(minutes=0.1)
}

with DAG(
    dag_id="first_dag_v3",
    description="Mon Premier DAG",
    default_args=default_args,
    start_date=datetime(2022,8,1),
    schedule_interval='@daily'
) as dag:
    task1 = BashOperator(
        task_id='first_task',
        bash_command="echo hello worl, c'est ma premiere tache avec Airflow"
    )

    task2 = BashOperator(
        task_id='secon_task',
        bash_command="echo hello worl, c'est ma seconde tache avec Airflow"
    )

    task3 = BashOperator(
        task_id='second_task',
        bash_command="echo hello worl, c'est ma troisieme tache avec Airflow"
    )

    #Dépendance des Taches

    ##Méthode 1
    task1 >> task2
    task1 >> task3

    ##Méthode 2
    #task1 >> [task2, task3]
