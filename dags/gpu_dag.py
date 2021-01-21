from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.utils.dates import days_ago
import docker

default_args = {
    'start_date': days_ago(2),
    'retries': 0,
}

with DAG(
        dag_id='gpu_docker_dag',
        schedule_interval=None,
        default_args=default_args,
    ) as dag:

    no_gpu = DockerOperator(
        task_id='no_gpu',
        image='nvidia/cuda:11.0-base',
        command="nvidia-smi",          
    )

    with_gpu = DockerOperator(
        task_id='with_gpu',
        image='nvidia/cuda:11.0-base',
        device_requests=[
            docker.types.DeviceRequest(count=-1, capabilities=[['gpu']])
        ]            
    )