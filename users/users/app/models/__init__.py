import psycopg2

DB_HOST = "localhost"
DB_PORT = "9999"
DB_NAME = "sotsuken_users"
DB_USER = "postgres"
DB_PASS = ""


# db = psycopg2.connect('host name', 'db name', 'scheme', 'user name', 'password')


def get_connection():
    return psycopg2.connect('postgresql://{user}:{password}@{host}:{port}/{dbname}'
        .format(
        user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT, dbname=DB_NAME
    ))

#
# conn = get_connection()
# cur = conn.cursor()
