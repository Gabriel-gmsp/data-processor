import destino
from mysql.connector import connect

class MysqlDestination(destino.TargetInterface):
    def __init__(self, host, user, password, database, table):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.table = table
    def save_data(self,data):
        
        connection = connect(host=self.host,
                             user=self.user,
                             password=self.password,
                             database=self.database)
        cursor = connection.cursor()
        for row in data:
            insert_query = (f"INSERT INTO {self.table} VALUES {str(tuple(row))}")
            cursor.execute()
        connection.commit()
