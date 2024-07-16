import mysql.connector

connection = mysql.connector.connect(
    host = 'localhost',
    user = 'auth-api',
    password = 'sql#117090',
    database = 'world'
)