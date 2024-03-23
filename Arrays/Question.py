#is it possible for an array to have different elements?
# No, by definition, an array cannot have elements of different data types.
# structures / classes can be used

class Item:
    def __init__(self, name, value):
        self.name = name
        self.value = value

mixed_data = [Item("apple", 10), Item("banana", 2.5)]
print(mixed_data[0].name)