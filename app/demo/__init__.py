import logging
import os

import boto3
import psycopg2
from botocore.client import BaseClient
from psycopg2._psycopg import connection

S3_HOST = "http://s3:9000"
DEFAULT_DB_POSTGRES = "default_db"
DB_HOST = "db"


logging.basicConfig(
    format="%(asctime)s %(levelname)-1s [%(filename)s:%(lineno)d] - %(message)s",
    level=logging.DEBUG,
)


def s3_client(
    endpoint_url: str,
    aws_access_key_id: str,
    aws_secret_access_key: str,
    region_name: str,
) -> BaseClient:
    return boto3.client(
        service_name="s3",
        region_name=region_name,
        endpoint_url=endpoint_url,
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
    )


def db_connection(database: str, host: str, port: str = "5432") -> connection:
    return psycopg2.connect(
        database=database,
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
        host=host,
        port=port,
    )
