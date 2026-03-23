from abc import ABC, abstractmethod

class RelationshipBrowser(ABC):
    @abstractmethod
    def find_all_children_of(self, name):
        pass