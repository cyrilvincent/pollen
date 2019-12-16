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

import re
class Book(Media):
    def __init__(self, id, title, price, date=datetime.datetime.now(), publisher: Publisher = None,
                 authors: List[Author] = [], nbPage = 0, isbn=None):
        super().__init__(id,title,price,date,publisher,authors)
        self._isbn = isbn
        self.nbPage = nbPage

    # @property
    # def netPrice(self):
    #     return self.price * 1.05 * 0.95 + 0.01

    @property
    def isbn(self):
        return self._isbn

    @isbn.setter
    def isbn(self, value):
        regex = r"^(\d{3}[- ]?)?\d[- ]?\d{4}[- ]?\d{4}[- ]?\d$"
        if re.search(regex, value):
            self._isbn = value
        else:
            raise ValueError("Bad ISBN format")

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

import abc
from typing import Iterable
class MediaRepository(metaclass=abc.ABCMeta):

    def __init__(self, uri):
        self.uri = uri

    @abc.abstractmethod
    def getAll(self) -> Iterable[Media]: ...

    @abc.abstractmethod
    def getByPrice(self): ...

import sqlite3
class MediaDb(MediaRepository):

    def __init__(self, uri):
        super().__init__(uri)

    def _getBySql(self, sql, conn):
        c = conn.cursor()
        return c.execute(sql)

    def _mapCursorToBook(self, row):
        b = Book(row[0], row[1], row[2])
        return b

    def getAll(self):
        with sqlite3.connect(self.uri) as conn:
            rows = self._getBySql("select * from book", conn)
            return (self._mapCursorToBook(row) for row in rows)

    def getByPrice(self, price):
        with sqlite3.connect(self.uri) as conn:
            rows = self._getBySql(f"select * from book where price <= {price}", conn)
            return (self._mapCursorToBook(row) for row in rows)






