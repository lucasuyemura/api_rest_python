import mysql.connector, json, jsonify


# URL de conexão com banco de dados local 

def connect(schema = "world", table = "city", consulta_sql = "SELECT * FROM"):
        
        return mysql.connector.connect(
            host = 'localhost',
            user = 'auth-api',
            password = 'sql#117090',
            database = schema
        )


def cursor():
        
         return connect().cursor()
         