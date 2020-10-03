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
