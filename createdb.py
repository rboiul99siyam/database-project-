import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="admin1234"

)
query = "CREATE DATABASE  SCHOOLS"
cursors = connection.cursor()
cursors.execute(query)
