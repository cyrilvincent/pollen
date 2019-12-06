class Author:

    def __init__(self, name):
        self.name = name

class Publisher:

    def __init__(self, name):
        self.name = name

import datetime
import abc
from typing import List
class Media(metaclass=abc.ABCMeta):

    def __init__(self, id, title, price, date = datetime.datetime.now(), publisher : Publisher = None, authors:List[Author] = []):
        self.id = id
        self.title = title
        self.price = price
        self.date = date
        self.publisher = publisher
        self.authors = authors

    @property
    @abc.abstractmethod
    def netPrice(self): ...

    def __repr__(self):
        return f"{type(self).__name__}: {self.id} {self.title}"

class Book(Media):
    def __init__(self, id, title, price, date=datetime.datetime.now(), publisher: Publisher = None,
                 authors: List[Author] = [], nbPage = 0):
        super().__init__(id,title,price,date,publisher,authors)
        self.nbPage = nbPage

    # @property
    # def netPrice(self):
    #     return self.price * 1.05 * 0.95 + 0.01


class Cd(Media):
    def __init__(self, id, title, price, date=datetime.datetime.now(), publisher: Publisher = None,
                 authors: List[Author] = [], nbTrack=0):
        super().__init__(id, title, price, date, publisher, authors)
        self.nbTrack = nbTrack

    @property
    def netPrice(self):
        return self.price * 1.2 * 0.9

import functools
class Cart:

    def __init__(self):
        self.medias = []

    def add(self, media:Media):
        self.medias.append(media)

    def remove(self, media:Media):
        self.medias.remove(media)

    @property
    def totalNetPrice(self):
        return sum([m.netPrice for m in self.medias])

    @property
    def totalNetPrice2(self):
        return functools.reduce(lambda acc, cur : acc + cur.netPrice, self.medias, 0)




