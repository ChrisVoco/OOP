from interfaces import *

class MyPrinter(Printer):
    def print(self, document):
        print(f"Printing: {document}")

class Photocopier(Printer, Scanner):
    def print(self, document):
        print(f"Printing: {document}")
    def scan(self, document):
        print(f"Scanning: {document}")

class MultiFunctionMachine:
    def __init__(self, printer: Printer, scanner: Scanner):
        self.printer = printer
        self.scanner = scanner

    def print(self, document):
        self.printer.print(document)

    def scan(self, document):
        self.scanner.scan(document)
