import time
from abc import ABCMeta, abstractmethod


class Observer(metaclass=ABCMeta):
    @abstractmethod
    def update(self, ganerator):
        pass


class DigitObserver(Observer):
    def update(self, generator):
        print("DigitObservser: {0}".format(generator.get_number()))
        time.sleep(0.1)


class GraphObserver(Observer):
    def update(self, generator):
        print("GraphicObserver:", end='')
        count = generator.get_number()
        for _ in range(count):
            print('*', end='')
        print("")
        time.sleep(0.1)


class SuggestionedObserver(Observer):
    def __init__(self, uuid):
        self.__uuid = uuid

    def update(self, generator):
        uuid = generator.get_uuid()
        if uuid != "" and uuid == self.__uuid:
            print("success")
            return
        print("failed")
