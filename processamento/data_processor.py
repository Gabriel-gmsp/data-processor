import abc
import time

class DataProcessor(metaclass=abc.ABCMeta): #Classe abstrata para processamento de dados
    def __init__(self, source):
        
        # Inicializa um objeto DataProcessor.
        # Args:
        # source: Fonte de dados a ser processada.
        # target: Destino onde os dados processados serão salvos.
        
        self.source = source

    def process(self): # Coordena o processo de processamento de dados
        start_time = time.time()
        data = self.source.get_data()
        processed_data = self.process_data(data)
        self.save_data(processed_data)
        end_time = time.time()
        print(f"{self.__class__.__name__} took {end_time - start_time} seconds to process.")
    
    @abc.abstractclassmethod
    def save_data(self, data):
        pass
        

    @abc.abstractmethod
    def process_data(self, data):
        pass