class Vector:
    def __init__(self):
        self._capacity = 16       # start at 16
        self._size = 0
        self._data = [None] * self._capacity

    def size(self):         # number of items stored
        return self._size

    def capacity(self):     # total allocated slots
        return self._capacity

    def is_empty(self):     # True if size == 0
        if self._size == 0:
            return True
        return False

    def at(self, index):    # get item, raise error if out of bounds
        if index < 0 or index <= self._capacity:
            raise IndexError
        return self._data[index]

    def push(self, item):   # add to end, resize if needed
        if self._size == self._capacity:
            self._resize(self._capacity * 2)
        self._data[self._size] = item
        self._size += 1

    def insert(self, index, item):
        if index < 0 or index >= self._size:
            raise IndexError
        if self._size == self._capacity:
            self._resize(self._capacity * 2)
        for i in range(self._size - 1, index - 1, -1):
            self._data[i + 1] = self._data[i]
        self._data[index] = item
        self._size += 1

    def prepend(self, item):        # insert at index 0
        self.insert(0, item)

    def pop(self):          # remove from end, return value
        last = self._data[self._size-1]
        self._data[self._size - 1 ] = None
        self._size -= 1
        if self._size <= self._capacity // 4:
            self._resize(self._capacity // 2)
        return last

    def delete(self, index):        # shift left after removal
        if index < 0 or index >= self._size:
            raise IndexError
        for i in range(index,self._size - 1):
            self._data[i] = self._data[i+1]
        self._data[self._size - 1] = None
        self._size -= 1
        if self._size <= self._capacity // 4:
            self._resize(self._capacity // 2)

    def remove(self, item): # remove ALL occurrences by value
        i = 0
        while i < self._size:
                if self._data[i] == item:
                    self.delete(i)
                else:
                    i += 1

    def find(self, item):   # return first index, or -1
        for i in range(self._size):
            if self._data[i] == item:
                return i
        return -1

    def _resize(self, new_capacity):  # private — double or halve
        temp = [None] * new_capacity
        for i in range(self._size):
            temp[i] = self._data[i]
        self._data = temp
        self._capacity = new_capacity