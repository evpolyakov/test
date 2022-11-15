from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator
from airflow.contrib.kubernetes.volume_mount import VolumeMount
from airflow.contrib.kubernetes.volume import Volume
from airflow.kubernetes.secret import Secret
from airflow import DAG
from airflow.utils.dates import days_ago

args = {
    "project_id": "untitled-1115102258",
}

dag = DAG(
    "untitled-1115102258",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="""
Created with Elyra 3.12.0 pipeline editor using `untitled.pipeline`.
    """,
    is_paused_upon_creation=False,
)


# Operator source: Untitled.ipynb

op_0553c398_0c30_4e82_9dcc_d6b7432275b4 = KubernetesPodOperator(
    name="Test",
    namespace="dept-ml",
    image="continuumio/anaconda3:2021.11",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.12.0/elyra/airflow/bootstrapper.py' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.12.0/elyra/airflow/bootstrapper.py --output bootstrapper.py && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.12.0/etc/generic/requirements-elyra.txt' && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.12.0/etc/generic/requirements-elyra-py37.txt' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.12.0/etc/generic/requirements-elyra-py37.txt --output requirements-elyra-py37.txt && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.12.0/etc/generic/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --pipeline-name 'untitled' --cos-endpoint http://minio-dept-ml.dept-ml:9000 --cos-bucket test --cos-directory 'untitled-1115102258' --cos-dependencies-archive 'Untitled-0553c398-0c30-4e82-9dcc-d6b7432275b4.tar.gz' --file 'Untitled.ipynb' "
    ],
    task_id="Test",
    env_vars={
        "ELYRA_RUNTIME_ENV": "airflow",
        "AWS_ACCESS_KEY_ID": "polyakov",
        "AWS_SECRET_ACCESS_KEY": "polyakov",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "ELYRA_RUN_NAME": "untitled-{{ ts_nodash }}",
    },
    volumes=[],
    volume_mounts=[],
    secrets=[],
    annotations={},
    labels={},
    tolerations=[],
    in_cluster=True,
    config_file="None",
    dag=dag,
)

op_0553c398_0c30_4e82_9dcc_d6b7432275b4.doc = """
        Test
    """
