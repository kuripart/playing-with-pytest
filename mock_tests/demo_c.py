import time
REST = 4

class Foo:
    def __init__(self):
        self.foo = None

    def load_foo(self):
        time.sleep(REST)
        self.foo = 'foo'


def bar():
    foo = Foo()
    return foo.load_foo()
