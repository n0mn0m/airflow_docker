from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta


default_args = {
    "owner": "alex",
    "depends_on_past": False,
    "start_date": datetime(2018, 12, 24),
    "email": ["alex@unexpectedeof.net"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

dag = DAG(
    "ssl-renewal", default_args=default_args, schedule_interval=timedelta(days=80)
)

t1 = BashOperator(task_id="certbot-renewal", bash_command="certbot renew", dag=dag)
