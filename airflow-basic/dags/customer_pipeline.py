from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import re

def validate_email(email: str) -> bool:
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return bool(re.match(pattern, email))


def extract_email(**context):
    dag_run = context.get("dag_run")

    email = None
    if dag_run and dag_run.conf:
        email = dag_run.conf.get("email")

    if not email:
        raise ValueError("Email not provided in DAG run config")

    return email

def validate(**context):
    ti = context["ti"]
    email = ti.xcom_pull(task_ids="extract_email")

    if not validate_email(email):
        raise ValueError(f"Invalid email: {email}")

    return email


def send_email(**context):
    ti = context["ti"]
    email = ti.xcom_pull(task_ids="validate_email")

    print(f" Email successfully sent to: {email}")


with DAG(
    dag_id="customer_email_pipeline",
    start_date=datetime(2024, 1, 1),
    schedule=None,   # manual trigger
    catchup=False,
    tags=["email", "pipeline"]
) as dag:

    extract_email_task = PythonOperator(
        task_id="extract_email",
        python_callable=extract_email
    )

    validate_email_task = PythonOperator(
        task_id="validate_email",
        python_callable=validate
    )

    send_email_task = PythonOperator(
        task_id="send_email",
        python_callable=send_email
    )

    extract_email_task >> validate_email_task >> send_email_task