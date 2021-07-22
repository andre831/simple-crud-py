import psycopg2

def dataUpdate(name,  employeeId):
    try:
        connection = psycopg2.connect(user     = "postgres",
                                  password = "deesantos123",
                                  host     = "localhost",
                                  port     = "5432",
                                  database ="postgresdb")

        cursor = connection.cursor()
        build_update = """Update employee set name = %s where id = %s"""
        cursor.execute(build_update, (employeeId,name))
        connection.commit()
        count = cursor.rowcount
        print(count, 'deu certo')

    except(Exception, psycopg2.Error) as error:
        print(error)

id = 3
name = 'Maria cabeç de pikkkk'
dataUpdate(id, name)