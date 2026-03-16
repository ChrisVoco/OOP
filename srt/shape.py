from abc import *


class Shape(ABC):
    @property
    @abstractmethod
    def area(self):
        pass