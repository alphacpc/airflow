from datetime import datetime, timedelta


from airflow.decorators import dag, task


default_args = {
    'owner':'alphacpc',
    'retries':3,
    'retry':timedelta(minutes=0.1)
}

@dag(
    dag_id="dag_with_taskflow_api",
    default_args=default_args,
    schedule_interval="@daily",
    start_date=datetime(2022,8,3)
)
def hello_world_etl():

    @task()
    def get_name():
        return 'alpha'

    @task()
    def get_plat():
        return 'Mafe'

    @task()
    def greet(name, plat):
        print(f"Je m'appelle {name} et j'aime le {plat}")


    name = get_name()
    plat = get_plat()
    greet(name=name, plat=plat)

greet_dag = hello_world_etl()