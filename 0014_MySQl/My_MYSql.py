import mysql.connector

# можно открыть через with
# лучше хранить в документе и его считывать
my_connection=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd=r'@Evp12345',
    database='sakila'
)
# my_connection=True
# student1=('Jack',20)
# mycursor=my_connection.cursor()
# #mycursor.execute('CREATE DATABASE python11')
# #mycursor.execute('CREATE TABLE student (name VARCHAR(100), age INTEGER(10))')
# mycursor.execute('INSERT INTO student (name,age) VALUES (%s,%s)',student1)
# mycursor.executemany('INSERT INTO student (name,age) VALUES (%s,%s)',student1)

my_connection.autocommit=True
mycursor=my_connection.cursor()

mycursor.execute('Select * From actor')
result=mycursor.fetchone() # брать по одному через цикл
print(result)
result=mycursor.fetchall() # брать все кортеджи
print(result)

result=mycursor.fetchmany(10) # количество
print(result)


#my_connection.commit()
#print(my_connection)
