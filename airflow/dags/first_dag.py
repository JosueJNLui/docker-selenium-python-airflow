"""
primeira DAG v0: Hello World!
"""
from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator, BranchPythonOperator
from datetime import datetime
import pandas as pd
import requests
import json

def captura_conta_dados():

    url = 'https://data.cityofnewyork.us/resource/rc75-m7u3.json'
    response = requests.get(url)
    df = pd.DataFrame(json.loads(response.content))
    qtd = len(df.index)
    return qtd

def e_valida(ti):

    qtd = ti.xcom_pull(task_ids = 'captura_conta_dados')
    if (qtd > 1000):
        return 'valido'
    return 'nao_valido'

with DAG(
    dag_id = "a_primeira_DAG_v0",
    start_date = datetime(2024,5,6),
    schedule_interval = "@daily",
    catchup = False,
    doc_md = __doc__
):
    # start = EmptyOperator(task_id='start')
    # hello = BashOperator(task_id='hello', bash_command="echo hello world")
    # end = EmptyOperator(task_id='end')

    captura_conta_dados = PythonOperator(
        task_id = "captura_conta_dados",
        python_callable = captura_conta_dados
    )

    e_valida = BranchPythonOperator(
        task_id = "e_valida",
        python_callable = e_valida
    )

    valido = BashOperator(
        task_id = "valido",
        bash_command = "echo 'Quantidade OK'"
    )

    nao_valido = BashOperator(
        task_id = "nao_valido",
        bash_command = "echo 'Quantidade NÃO OK'"
    )

(captura_conta_dados >> e_valida >> [valido, nao_valido])
# (start >> hello >> end)
