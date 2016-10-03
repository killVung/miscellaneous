class HelloWorld:
    def __iter__(self):
        yield 'H'
        yield 'e'
        yield 'l'
        yield 'l'
        yield 'o'
        yield 'W'
        yield 'o'
        yield 'r'
        yield 'l'
        yield 'd'
        yield '!'
for i in HelloWorld():
    print(i,end="")
