class Wspak:
    """Iterator zwracający wartości w odwróconym porządku"""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

text = "Python"
wspak = Wspak(text)
print(wspak.__next__())
print(wspak.__next__())
print(wspak.__next__())
print(wspak.__next__())
print(wspak.__next__())
print(wspak.__next__())

print("####")

tab = [1, 2, 3, 4, 5]
wspak2 = Wspak(tab)
print(wspak2.__next__())
print(wspak2.__next__())
print(wspak2.__next__())
print(wspak2.__next__())
print(wspak2.__next__())