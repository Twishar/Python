
from contextlib import contextmanager

with open('hello.txt', 'w') as f:
    f.write('hello, world!')


# The same

f = open('hello.txt', 'w')
try:
    f.write('hello, world')
finally:
    f.close()


class ManagedFile:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        self.file = open(self.name, 'w')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()


with ManagedFile('hello.txt') as f:
    f.write('hello, world!')
    f.write('bye now')


# Same for context manager

@contextmanager
def managed_file(name):
    try:
        f = open(name, 'w')
        yield f
    finally:
        f.close()


with managed_file('hello.txt') as f:
    f.write('hello, world!')
    f.write('bye now')


class Indenter:
    def __init__(self):
        self.level = 0

    def __enter__(self):
        self.level += 1
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.level -= 1

    def print(self, text):
        print('     ' * self.level + text)


with Indenter() as indent:
    indent.print('hi!')
    with indent:
        indent.print('hello')
        with indent:
            indent.print('bonjour')
    indent.print('hey')
