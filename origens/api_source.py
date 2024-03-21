
import requests
import origens
       
class APISource(origens.SourceInterface):
    
    def __init__(self, url):
        
        self.url = url
        
    def get_data(self):
        
        response = requests.get(self.url)
        
        if response.status_code == 200:
            
            return response.json()
        
        else:
            print(f'Error ocurred: {response.status_code}')
                