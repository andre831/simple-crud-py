import psycopg2
from psycopg2 import Error


try:
    connection = psycopg2.connect(user     = "postgres",
                                  password = "deesantos123",
                                  host     = "localhost",
                                  port     = "5432",
                                  database ="postgresdb")

    cursor = connection.cursor()

    print("Postgres ta rodando")
    print(connection.get_dsn_parameters(), "\n")

    cursor.execute("SELECT version();")

    #search results
    record = cursor.fetchone()
    print("I'm connected to Postgres", record)

    #SQL query table
    table_build = '''CREATE TABLE tasks
            (ID              SERIAL       PRIMARY KEY,
             NAME            TEXT         NOT NULL,
             DATE            TEXT         NOT NULL,
             DESCRIPTION     TEXT         NOT  NULL);'''
    cursor.execute(table_build)
    connection.commit()
    print("Table conclude")

except (Exception, Error) as error:
    print("Error in connect from Postgres")

finally:
    if (connection):
        cursor.close()
        connection.close()
        print("Postgres fechou")