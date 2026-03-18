
if __name__ == "__main__":
    from interfaces import *
    from device import *

printer = MyPrinter()
photocopier = Photocopier()

printer.print("Hello from printer")

photocopier.print("Copy this document")
photocopier.scan("Scanned document")

mfm = MultiFunctionMachine(printer, photocopier)
mfm.print("Delegated print")
mfm.scan("Delegated scan")