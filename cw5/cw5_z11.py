def fib():
    a = 0
    b = 1
    while True:
        yield a
        tmp = a
        a = b
        b = tmp + b

f = fib()
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())