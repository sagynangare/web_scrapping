def logger(func):
    def inner(*args, **kwargs):
        print("Arguments were: %s, %s" %(args, kwargs))
        return func(*args, **kwargs)
    return inner
@logger
def foo_1(x, y=3):
    return 2
@logger
def foo2():
    return 2

foo_1(5,4)
print("@##%##@"*8)
foo2()
