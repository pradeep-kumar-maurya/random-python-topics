from abc import ABC, abstractmethod


class OldPrinterFunctionality(ABC):
    
    @abstractmethod
    def print_content(content: str):
        pass

    @abstractmethod
    def scan_content(content: str):
        pass

    @abstractmethod
    def photocopy_content(content: str):
        pass


# Creating a separate interface for new printers resolves the problem of unwanted implementations
class NewPrinterFunctionality(ABC):

    @abstractmethod
    def fax_content(content: str):
        pass

    @abstractmethod
    def print_duplex_content(content: str):
        pass


class OldPrinter(OldPrinterFunctionality):

    def print_content(self, content: str):
        print(f"old printer printing: {content}")

    def scan_content(self, content: str):
        print(f"old printer scanning: {content}")

    def photocopy_content(self, content: str):
        print(f"old printer phtocopying: {content}")


# new printer can implement both the printer functionalies i.e. old and new
class NewPrinter(NewPrinterFunctionality, OldPrinterFunctionality):

    def fax_content(self, content: str):
        print(f"new printer faxing: {content}")

    def print_duplex_content(self, content: str):
        print(f"new printer printing duplex: {content}")

    def print_content(self, content: str):
        print(f"new printer printing: {content}")

    def scan_content(self, content: str):
        print(f"new printer scanning: {content}")

    def photocopy_content(self, content: str):
        print(f"new printer phtocopying: {content}")


old = OldPrinter()
old.print_content("printing content from old printer")
old.scan_content("scanning content from old printer")
old.photocopy_content("photocopying data from old printer")


new = NewPrinter()
new.fax_content("this is my bio data")
new.print_duplex_content(
    '''
    My Name is Pradeep.
    I work at Deloitte.
    I want to work hard for my dreams.
    '''
    )
new.print_content("printing content from new printer")
new.scan_content("scanning content from new printer")
new.photocopy_content("photocopying data from new printer")
