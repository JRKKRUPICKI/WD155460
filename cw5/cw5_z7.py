class PIndex:

    def __init__(self, data):
        self.data = data
        self.index = -2

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index + 2 > len(self.data) - 1:
            raise StopIteration
        self.index +=2
        return self.data[self.index]

tab = [1, 2, 3, 4, 5, 6, 7]
pix = PIndex(tab)
print(pix.__next__())
print(pix.__next__())
print(pix.__next__())
print(pix.__next__())