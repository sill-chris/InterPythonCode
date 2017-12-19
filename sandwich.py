def bread(func):
    def wrapper():
        print("</''''''\>")
        func()
        print("<\______/>")

    return wrapper


def ingredients(func):
    def wrapper():
        print("#tomatoes#")
        print("!!pickle!!")
        func()
        print("~lettuce~")
    return wrapper


@bread
@ingredients
def sandwich(food = "---ham---"):
    print(food)

if __name__ == '__main__':
    sandwich()
