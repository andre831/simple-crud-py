import psycopg2

def dataDel(tasksId):
    try:
        connection = psycopg2.connect(user     = "postgres",
                                      password = "deesantos123",
                                      host     = "localhost",
                                      port     = "5432",
                                      database = "postgresdb")
        cursor = connection.cursor()

        delete_build = "DELETE FROM tasks where id = %s"
        cursor.execute(delete_build,  (tasksId, ))
        connection.commit()
        count = cursor.rowcount
        print(count, "Deleted record" "\n")

    except (Exception, psycopg2.Error) as error:

        print(error)


    finally:
        if connection:
            cursor.close()

            connection.close()

    print("PostgreSQL connection is closed")

deltasks = 5
dataDel(deltasks)
