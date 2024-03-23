from processamento.data_processor import DataProcessor
from origens.csv_source import CsvSouuce
from destino.mysql_destination import MysqlDestination

class ProcessCenso(DataProcessor):
    
    def __init__ (self):
        
        csv_source = CsvSouuce(file_path=" ")
        
    
    def process_data(self):
        
        pass
    
    def save_data(self,data):
        
        mysql_destino = MysqlDestination(host="", user="", password="", database="")
            
        
        
        