import random
import uuid as uuid
from abc import ABCMeta, abstractmethod, ABC


class NumberGenerator(metaclass=ABCMeta):
    def __init__(self):
        self.__observers = []

    def add_observer(self, observer):
        self.__observers.append(observer)

    def delete_observer(self, observer):
        self.__observers.remove(observer)

    def notify_observer(self):
        for o in self.__observers:
            o.update(self)

    @abstractmethod
    def get_number(self):
        pass

    @abstractmethod
    def execute(self):
        pass


class RandomNumberGenerator(NumberGenerator, ABC):
    def __init__(self):
        self.__number = 0
        super(RandomNumberGenerator, self).__init__()

    def get_number(self):
        return self.__number

    def execute(self):
        for _ in range(20):
            self.__number = random.randint(0, 49)
            self.notify_observer()


class EventGenerator(NumberGenerator, ABC):
    def __init__(self):
        self.__uuid = str(uuid.uuid4())
        super(EventGenerator, self).__init__()

    def get_number(self):
        pass

    def get_uuid(self):
        return self.__uuid

    def execute(self):
        # self.__uuid = str(uuid.uuid4())
        # print(self.__observers)
        self.notify_observer()
