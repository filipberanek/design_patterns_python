# ISP principle
from abc import abstractmethod


class Machine:
    def print(self, document):
        raise NotImplementedError

    def fax(self, document):
        raise NotImplementedError

    def scan(self, document):
        raise NotImplementedError


class MultifunctionalPrinter(Machine):
    def print(self, document):
        pass

    def fax(self, document):
        pass

    def scan(self, document):
        pass


class OldFashionedPrinter(Machine):
    def print(self, document):
        # ok
        pass

    def fax(self, document):
        # noop
        pass

    def scan(self, document):
        # noop
        raise NotImplementedError("Printer cannot scan!")


# What you want to do is split interface into granular interfaces


class Printer:
    @abstractmethod
    def print(self, document):
        raise NotImplementedError


class Fax:
    @abstractmethod
    def fax(self, document):
        raise NotImplementedError


class Scanner:
    @abstractmethod
    def scan(self, document):
        raise NotImplementedError


class Photocopier(Printer, Scanner):
    def print(self, document):
        pass

    def scan(self, document):
        pass


class MultifunctionDevice(Printer, Scanner, Fax):
    def print(self, document):
        pass

    def scan(self, document):
        pass

    def fax(self, document):
        pass
