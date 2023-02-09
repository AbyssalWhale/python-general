from abc import ABC, abstractmethod

# All abstract classes must be inherited from ABC
class Stream(ABC):

    # @abstractmethod - decorator is used to declare abstract methods
    @abstractmethod
    def read(self):
        print("Reading from default stream...")


class MemoryStream(Stream):
    def read(self):
        print("Reading from memoring stream...")


M_STREAM = MemoryStream()
M_STREAM.read()
