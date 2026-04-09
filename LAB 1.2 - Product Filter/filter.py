from abc import ABC, abstractmethod


class Filter(ABC):
    @abstractmethod
    def filter(self, items, spec):
        pass


class BetterFilter(Filter):
    def filter(self, items, spec):
        for item in items:
            if spec.is_satisfied(item):
                yield item