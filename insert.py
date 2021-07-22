import psycopg2

try:
    connection = psycopg2.connect(user     = "postgres",
                                  password = "deesantos123",
                                  host     = "localhost",
                                  port     = "5432",
                                  database ="postgresdb")

    cursor = connection.cursor()

    insert_build = """ INSERT INTO employee (NAME, ROLE, TURN) VALUES (%s,%s,%s) """

    employee_build2 = ("Melissa", "Dev. Angular", "noite")

    cursor.execute(insert_build, employee_build2)

    connection.commit()
    count = cursor.rowcount
    print(count, "Record inserted successfully into employee table" "\n")

except (Exception, psycopg2.Error) as error:
    print(error)

finally:
    # closing database connection.
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")