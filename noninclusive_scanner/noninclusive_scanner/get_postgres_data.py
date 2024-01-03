import sys

import psycopg2 as pg
import pandas.io.sql as psql

def get_now(db_connect):

    # Schema name can also be parameterized
    sql = "SELECT distinct t1.table_schema, t1.table_name, t1.table_type, t2.column_name " \
          "FROM information_schema.tables t1 " \
          "join information_schema.columns t2 " \
          "on t1.table_schema = t2.table_schema " \
          "and t1.table_name = t2.table_name " \
          "where t1.table_schema = 'test_schema' " \
          "order by 1,2"

    connection = pg.connect(f"host={db_connect['host']} dbname={db_connect['database']} user={db_connect['user']} password={db_connect['password']}")
    df = psql.read_sql(sql, connection)
    return df