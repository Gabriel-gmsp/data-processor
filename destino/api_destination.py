from destino import TargetInterface
import requests


class APIDestination(TargetInterface):
    def __init__(self,url):
        self.url = url
    def save_data(self, data):
        response = requests.post(self.url, json=data)
        
        if response.status_code == 200:
            
            print('Data save successfully')
        
        else:
            
            print(f"Error occurred: {response.status_code}")