from abc import ABC,abstractmethod
class BaseAI(ABC):
    @abstractmethod
    def understand(self,message):
        pass