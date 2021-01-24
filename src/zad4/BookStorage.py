class BookStorage(object):
    def __init__(self, data=[]):
        self.__data = data

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    def find(self, book_id=None):
        if book_id == None:
            return self.data
        else:
            return self.data[book_id]
    
    def add(self, book):
        self.data.append(book)
        return True

    def delete(self, book):
        self.data.remove(book)
        return True