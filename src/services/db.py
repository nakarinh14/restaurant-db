import psycopg2
import psycopg2.extras
import os

class Database:
    connection = None
    def connect(self):
        try:
            if self.connection is None:
                self.connection = psycopg2.connect(
                    user = os.environ['DB_USER'],
                    password = os.environ['DB_PASSWORD'],
                    host = os.environ['DB_HOST'],
                    port = os.environ['DB_PORT'],
                    database = os.environ['DB_DATABASE']
                )
        except psycopg2.DatabaseError as e:
            print("Unable to connect :/")
            raise e
        return self.connection

    def execute_statement(self, statement: str, values=None):
        """General statement execution for DB."""
        connection = self.connect()
        cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
        if values:
            cursor.execute(statement, values)
        else:
            cursor.execute(statement)
        return cursor

    def retrive_rows(self, statement: str, values=None):
        """Run a SQL query to retrieve rows in table."""
        cursor = self.execute_statement(statement, values)
        results = cursor.fetchall()
        cursor.close()
        return results

    def retrive_single(self, statement: str):
        """Run a SQL query to retrieve a single row in table."""
        cursor = self.execute_statement(statement)
        results = cursor.fetchone()
        cursor.close()
        return results
    
    def write_rows(self, statement: str):
        """Run a SQL query to update rows in table."""
        cursor = self.execute_statement(statement)
        self.connection.commit()
        cursor.close()
        return f"{cursor.rowcount} rows affected."
