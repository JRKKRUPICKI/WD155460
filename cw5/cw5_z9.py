def pindex(data):
    for i in range(0, len(data), 2):
        yield data[i]

tab = [1, 2, 3, 4, 5, 6, 7]
pix = pindex(tab)
print(pix.__next__())
print(pix.__next__())
print(pix.__next__())
print(pix.__next__())