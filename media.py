class Author:

    def __init__(self, name):
        self.name = name

class Publisher:

    def __init__(self, name):
        self.name = name

import datetime
from typing import List
class Media:

    def __init__(self, id, title, price, date = datetime.datetime.now(), publisher : Publisher = None, authors:List[Author] = []):
        self.id = id
        self.title = title
        self.price = price
        self.date = date
        self.publisher = publisher
        self.authors = authors

    @property
    def netPrice(self):
        return self.price * 1.2

    def __repr__(self):
        return f"{type(self).__name__}: {self.id} {self.title}"

class Book(Media):
    def __init__(self, id, title, price, date=datetime.datetime.now(), publisher: Publisher = None,
                 authors: List[Author] = [], nbPage = 0):
        super().__init__(id,title,price,date,publisher,authors)
        self.nbPage = nbPage

    @property
    def netPrice(self):
        return self.price * 1.05 * 0.95 + 0.01


class Cd(Media):
    def __init__(self, id, title, price, date=datetime.datetime.now(), publisher: Publisher = None,
                 authors: List[Author] = [], nbTrack=0):
        super().__init__(id, title, price, date, publisher, authors)
        self.nbTrack = nbTrack

    @property
    def netPrice(self):
        return self.price * 1.2 * 0.9






