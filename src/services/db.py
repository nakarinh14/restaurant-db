import psycopg2
import psycopg2.extras


class Database:
    connection = None

    def connect(self):
        try:
            if self.connection is None:
                self.connection = psycopg2.connect(
                    user='postgres',
                    password='topsecret',
                    host='localhost',
                    port='5432',
                    database='food_review_db'
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

    def retrieve_rows(self, statement: str, values=None):
        """Run a SQL query to retrieve rows in table."""
        cursor = self.execute_statement(statement, values)
        results = cursor.fetchall()
        cursor.close()
        if results is None:
            results = []
        return [dict(r) for r in results]

    def retrieve_single(self, statement: str, values=None):
        """Run a SQL query to retrieve a single row in table."""
        cursor = self.execute_statement(statement, values)
        result = cursor.fetchone()
        cursor.close()
        if result is None:
            result = []
        return dict(result)

    def write_rows(self, statement: str):
        """Run a SQL query to update rows in table."""
        cursor = self.execute_statement(statement)
        self.connection.commit()
        cursor.close()
        return f"{cursor.rowcount} rows affected."

    def insert_row(self, statement: str, values=None):
        """Run a SQL query to add row to the table and return row id."""
        # Format: "INSERT INTO table(attr) VALUES (attr) RETURNING id.
        cursor = self.execute_statement(statement, values)
        add_id = cursor.fetchone()[0]
        self.connection.commit()
        cursor.close()
        return add_id

    def delete_row(self, statement: str, values=None):
        cursor = self.execute_statement(statement, values)
        self.connection.commit()
        cursor.close()
        return
