import psycopg2
import pandas as pd
from sqlalchemy import create_engine


def load(file, table_name):
    # read csv
    data = pd.read_csv(file, encoding='unicode_escape')

    user = input your username
    passwd = input your pass
    hostname = input your host
    database = input your database names

    conn_string = f'postgresql://{user}:{passwd}@{hostname}:5432/{database}'

    db = create_engine(conn_string)
    conn = db.connect()

    data.to_sql(table_name, con=conn, if_exists='append',
                index=False)

    #conn = psycopg2.connect(conn_string)

if __name__ == '__main__':
    load('import your file path', 'your desired table name')
