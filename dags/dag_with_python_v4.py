from datetime import timedelta, datetime
from airflow import DAG
from airflow.operators.python import PythonOperator

default_args = {
    'owner' : 'alphacpc',
    'retries' : 2,
    'retry_delay': timedelta(minutes=0.1)
}

def greet(ti):
    fname = ti.xcom_pull(task_ids='get_name', key='firstname')
    lname = ti.xcom_pull(task_ids='get_name', key='lastname').upper()
    plat = ti.xcom_pull(task_ids='get_plat', key='plat')

    print(f"Je m'appelle {fname} {lname}", f"et j'aime le {plat}")


def get_fullname(ti):
    ti.xcom_push(key="firstname", value="Kaba")
    ti.xcom_push(key="lastname", value="diallo")


def get_plat(ti):
    ti.xcom_push(key="plat", value="Mafé")


with DAG(
    default_args=default_args,
    dag_id="first_dag_python_operator_v4",
    description="Mon premier DAG python",
    start_date=datetime(2022, 8,3),
    schedule_interval="@daily"
) as dag:

    task1 = PythonOperator(
        task_id="greet_v3",
        python_callable=greet
    )

    task2 = PythonOperator(
        task_id="get_name",
        python_callable=get_fullname
    )

    task3 = PythonOperator(
        task_id="get_plat",
        python_callable=get_plat
    )


    [task2, task3] >> task1