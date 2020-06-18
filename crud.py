import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="blog"
)

if conn.is_connected():
    print("Connected")