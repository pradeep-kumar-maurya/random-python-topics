from abc import ABC, abstractmethod


class PrinterFunctionality(ABC):
    
    @abstractmethod
    def print_content(content: str):
        pass

    @abstractmethod
    def scan_content(content: str):
        pass

    @abstractmethod
    def photocopy_content(content: str):
        pass

    @abstractmethod
    def fax_content(content: str):
        pass

    @abstractmethod
    def print_duplex_content(content: str):
        pass


class OldPrinter(PrinterFunctionality):

    def print_content(self, content: str):
        print(f"old printer printing: {content}")

    def scan_content(self, content: str):
        print(f"old printer scanning: {content}")

    def photocopy_content(self, content: str):
        print(f"old printer phtocopying: {content}")

    '''
    The problem here is that the old printer has only three functionalities i.e. printing, scanning and photocopying the content.
    But due to big fat PrinterFunctionality interface, we need to implement fax_content and print_duplex_content method which
    are irrelevant to old printer.
    This is the problem which Interface Segregation Prociple from SOLID tries to resolve.
    '''


p = OldPrinter()
p.print_content("hello world")

