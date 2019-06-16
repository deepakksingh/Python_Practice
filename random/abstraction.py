from abc import ABC, abstractmethod

class AbstractClassExample(ABC):

    @abstractmethod
    def doSomething(self):
        print("Some basic implementation of the base class")

class AnotherSubClass(AbstractClassExample):
    def doSomething(self):
        super().doSomething()
        print("The enrichment provided from the child class")

x = AnotherSubClass()
x.doSomething()
