
# implement hash tables using classes
class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]

    def my_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % 100
    print(ord('a'))

t = HashTable()
t.my_hash('march 7')
