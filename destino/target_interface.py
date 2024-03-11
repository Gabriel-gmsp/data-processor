import abc

class TargetInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def save_data(self, data): # Método abstrato para salvar dados.
        pass
