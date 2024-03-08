import abc
import time
import csv
import requests
from mysql.connector import connect, Error

# Definindo uma interface para fontes de dados
class SourceInterface(metaclass=abc.ABCMeta): 
    @abc.abstractmethod
    def get_data(self):
        pass

class TargetInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def save_data(self, data): # Método abstrato para salvar dados.
        pass

class MysqlSource(SourceInterface):
    
    def __init__(self, host, user, password, database, table):
        
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.table = table
    
    def get_data(self):
        
        try:
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
        except Error as e:
            print(f'Error ocurred: {e}')
            
class CsvSouuce(SourceInterface):
    def __init__(self,file_path):
        
        self.file_path = file_path
    
    def get_data(self):
        
        with open(self.file_path, mode='r') as file:
            reader = csv.reader(file, delimiter=';')
            data = []
            for row in reader:
                data.append(row)
            return data
        
class APISource(SourceInterface):
    def __init__(self, url):
        
        self.url = url
        
    def get_data(self):
        
        response = requests.get(self.url)
        
        if response.status_code == 200:
            return response.json()
        else:
            print(f'Error ocurred: {response.status_code}')
                
                
                 
        











class DataProcessor(metaclass=abc.ABCMeta): #Classe abstrata para processamento de dados
    def __init__(self, source, target):
        
        # Inicializa um objeto DataProcessor.
        # Args:
        #     source: Fonte de dados a ser processada.
        #     target: Destino onde os dados processados serão salvos.
        
        self.source = source
        self.target = target

    def process(self): # Coordena o processo de processamento de dados
        start_time = time.time()
        data = self.source.get_data()
        processed_data = self.process_data(data)
        self.target.save_data(processed_data)
        end_time = time.time()
        print(f"{self.__class__.__name__} took {end_time - start_time} seconds to process.")

    @abc.abstractmethod
    def process_data(self, data):
        pass