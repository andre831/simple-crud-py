import psycopg2

def dataDel(employeeId):
    try:
        connection = psycopg2.connect(user     = "postgres",
                                      password = "deesantos123",
                                      host     = "localhost",
                                      port     = "5432",
                                      database = "postgresdb")
        cursor = connection.cursor()

        delete_build = "DELETE FROM employee where id = %s"
        cursor.execute(delete_build,  (employeeId, ))
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

delEmployee = 5
dataDel(delEmployee)
