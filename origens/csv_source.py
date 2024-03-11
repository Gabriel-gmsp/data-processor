import csv
import origens

class CsvSouuce(origens.SourceInterface):
    def __init__(self,file_path):
        
        self.file_path = file_path
    
    def get_data(self):
        
        with open(self.file_path, mode='r') as file:
            reader = csv.reader(file, delimiter=';')
            data = []
            for row in reader:
                data.append(row)
            return data