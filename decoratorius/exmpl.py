def smart_div(func):
    def inner(a, b):
        if b == 0:
            return print("Can't divide by 0")
        return func(a, b)
    return inner


@smart_div
def div(a, b):
    return a / b


# div = smart_div(div)

print(div(10, 0))


print("-" * 50)


def func(f):
    def wrapper(*args, **kwargs):
        print("Started")
        f(*args, **kwargs)
        print("Ended")

    return wrapper


@func
def func2(x, y):
    print(y, x)


@func
def func3():
    print("I am func3")


func3()
func2(5, 6)

print("-" * 50)


import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        rv = func()
        total = time.time() - start
        print("Time:", total)
        return rv

    return wrapper


@timer
def test():
    for _ in range(100000):
        pass


@timer
def test2():
    time.sleep(2)

test()
test2()