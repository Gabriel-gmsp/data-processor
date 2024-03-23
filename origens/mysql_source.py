import origens
from mysql.connector import connect

class MysqlSource(origens.SourceInterface):
    
    def __init__(self, host, user, password, database, table):
        
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.table = table
    
    def get_data(self):
               
        connection = connect(host=self.host,
                             user=self.user,
                             password=self.password,
                             database=self.database)
        
        cursor = connection.cursor()
        cursor.execute(f'SELECT * FROM {self.table}')
        data = cursor.fetchall()
        cursor.close()
        connection.close()
        return data