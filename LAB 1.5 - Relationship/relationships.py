from enum import Enum
from browser import RelationshipBrowser

class Relationship(Enum):
    PARENT = 1
    CHILD = 2
    SIBLING = 3

class Relationships(RelationshipBrowser):
    def __init__(self):
        self.relations = []

    def add_parent_and_child(self, parent, child):
        self.relations.append((parent, Relationship.PARENT, child))
        self.relations.append((child, Relationship.CHILD, parent))

    def find_all_children_of(self, name):
        for parent, relation, child in self.relations:
            if parent.name == name and relation == Relationship.PARENT:
                yield child