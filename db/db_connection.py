# dependency injection
# simgle resposability/god object
# page object
# singleton
# abstract pattern
# open close priciples
# method factory
import psycopg2


class DatabaseConnection:
    def __init__(self, dbname, user, password, host, port):
        self.connection = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
        )

    def execute(self, query, *args):
        with self.connection.cursor() as cursor:
            cursor.execute(query, args)
            self.connection.commit()

    def fetchone(self, query, *args):
        with self.connection.cursor() as cursor:
            cursor.execute(query, args)
            return cursor.fetchone()

    def close(self):
        self.connection.close()
