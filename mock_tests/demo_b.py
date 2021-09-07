import time

REST = 5

def foo_bar():
    time.sleep(REST)
    return REST

def foo():
    return foo_bar()
