import mysql.connector, json, jsonify

# URL de conexão com banco de dados local 
def connect(schema = "world"):
        
        my_db = mysql.connector.connect(
            host = 'localhost',
            user = 'auth-api',
            password = 'sql#117090',
            database = schema
        )

        return my_db

         