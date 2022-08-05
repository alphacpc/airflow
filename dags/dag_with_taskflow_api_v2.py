from datetime import datetime, timedelta


from airflow.decorators import dag, task


default_args = {
    'owner':'alphacpc',
    'retries':3,
    'retry':timedelta(minutes=0.1)
}

@dag(
    dag_id="dag_with_taskflow_api_v2",
    default_args=default_args,
    schedule_interval="@daily",
    start_date=datetime(2022,8,3)
)
def hello_world_etl():

    @task(multiple_outputs=True)
    def get_name():
        return {
            'fname':'Alpha',
            'lname':'diallo'
        }

    @task()
    def get_plat():
        return 'Mafe'

    @task()
    def greet(fname, lname, plat):
        print(f"Je m'appelle {fname} {lname} et j'aime le {plat}")


    name_dict = get_name()
    plat = get_plat()
    greet(fname=name_dict['fname'], lname=name_dict['lname'], plat=plat)

greet_dag = hello_world_etl()