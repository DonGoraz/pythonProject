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
    def wrapper():
        print("Started")
        f()
        print("Ended")

    return wrapper


@func
def func2():
    print("I am func2")


@func
def func3():
    print("I am func3")


func3()
func2()
