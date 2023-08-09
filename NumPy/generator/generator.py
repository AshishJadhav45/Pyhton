def fun():
    yield 'A'
    yield 'B'
    yield 'c'

f = fun()
print(type(f))

print(next(f))
print(next(f))
print(next(f))



