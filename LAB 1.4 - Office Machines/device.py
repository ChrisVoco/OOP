from interfaces import *

class MyPrinter(Printer):
    def print(self, document):
        print(f"Printing: {document}")

class Photocopier(Printer, Scanner):
    def print(self, document):
        print(f"Printing: {document}")
    def scan(self, document):
        print(f"Scanning: {document}")