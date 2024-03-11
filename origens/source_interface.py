import abc

# Definindo uma interface para fontes de dados
class SourceInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_data(self):
        pass
