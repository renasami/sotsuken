from abc import ABC

import psycopg2


def _execute(sql_state: str, cursor: any, *args: any):
    cursor.execute(sql_state, args)


class CommonModel(ABC):
    def __init__(self):
        self.connection = psycopg2.connect('postgresql://{user}:{password}@{host}:{port}/{dbname}'
            .format(
            user="postgres", password="", host="localhost", port="9999", dbname="sotsuken-users"
        ))

    def fetch_one(self, sql, *args):
        with self.connection.cursor() as c:
            _execute(sql, c, *args)
            return c.fetchone()
        pass

    def fetch_one_of_null(self, sql, *args):
        with self.connection.cursor() as cursor:
            _execute(sql, cursor, *args)
            return cursor.fetchone()

        pass

    def fetch_all(self, sql, *args):
        with self.connection.cursor() as cursor:
            _execute(sql, cursor, *args)
            return cursor.fetchall()

    def execute(self, sql, cursor, *args):
        with self.connection.cursor() as c:
            _execute(sql, cursor, *args)

    # def __del__(self):
    #     self.connection.close()
