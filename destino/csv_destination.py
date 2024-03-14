from destino import TargetInterface
import pandas as pd

class CSVDestination(TargetInterface):
    def __init__(self, file_path):
        self.file_path = file_path
        
    def save_data(self, data):
        df = pd.DataFrame(data)
        df.to.csv(self.file_path, index=False)