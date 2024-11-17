import psycopg2
from dotenv import load_dotenv
import os
from os.path import join, dirname


def get_from_env(key):
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)
    return os.environ.get(key)  # возвращен сеkркетный токен (или ключ к платежной системе)

def connect_db():
    connection = None
    try:
        # connect to exist database
        connection = psycopg2.connect(
            host=get_from_env('HOST'),
            user='postgres',
            password=get_from_env('PASSWORD'),
            database=get_from_env('DB_NAME')
        )
        connection.autocommit = True
    except Exception as _ex:
        print(f"user{get_from_env('USER')}")
        print("[INFO] Error while working with PostgreSQL", _ex)

    # the cursor for perfoming database operations
    cursor = connection.cursor()
    return cursor

def get_id(x):  # get customer_id from a table customers
    with connect_db() as cursor:  # open.py DB
        cursor.execute(
            f"SELECT customer_id FROM customers WHERE telegram_id = {x}"
        )

        y = cursor.fetchone()
        return y
