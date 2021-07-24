import psycopg2

connection = psycopg2.connect(user     = "postgres",
                                  password = "deesantos123",
                                  host     = "localhost",
                                  port     = "5432",
                                  database ="postgresdb")

cursor = connection.cursor()

pg2 = "SELECT * FROM tasks"

cursor.execute(pg2)
results = cursor.fetchall()

cursor.close()
connection.close()

for result in results:
    print(result)