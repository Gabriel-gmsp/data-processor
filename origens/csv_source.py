import pandas as pd
import origens

class CsvSouuce(origens.SourceInterface):
    def __init__(self,file_path):
        
        self.file_path = file_path
    
    def get_data(self):
        
        data = pd.read_csv(self.file_path)        
        return data.values.tolist
       