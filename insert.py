import psycopg2

try:
    connection = psycopg2.connect(user     = "postgres",
                                  password = "deesantos123",
                                  host     = "localhost",
                                  port     = "5432",
                                  database ="postgresdb")

    cursor = connection.cursor()

    insert_build = """ INSERT INTO tasks (NAME, DATE, DESCRIPTION) VALUES (%s, %s ,%s) """

    tasks_build = ("Trabalhar com o pai", "Sábado", "Ajudar nas tarefas para que tudo se resolva")

    cursor.execute(insert_build, tasks_build)

    connection.commit()
    count = cursor.rowcount
    print(count, "Record inserted successfully into tasks table" "\n")

except (Exception, psycopg2.Error) as error:
    print(error)

finally:
    # closing database connection.
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")