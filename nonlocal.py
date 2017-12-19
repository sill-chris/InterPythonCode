
message = 'global'


def enclosing():
    message = 'enclosing'

    def local():
        # nonlocal binds to 'enclosing'
        nonlocal message
        message = 'local'

    print("Enclosing mesage:", message)
    local()
    print("Enclosing mesage:", message)


if __name__ == '__main__':
    print('Global message:', message)
    enclosing()
    print('Global message:', message)