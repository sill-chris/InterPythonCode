
def escape_unicode(f):
    def wrap(*args, **kwargs):
        x = f(*args, **kwargs)
        return ascii(x)
    return wrap


@escape_unicode
def mexico_city():
    # ALT + 130 for é
    return "México"


def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print('Wrapper executed this before {}'.format(
            original_function.__name__))
        return original_function(*args, **kwargs)

    return wrapper_function


@decorator_function
def display():
    print("Display function ran")

# @decorator_function
# def display_info(name, age):
#     print("Display_info ran with parameters ({}, {})".format(name, age))

def my_logger(orig_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(
        orig_func.__name__), level=logging.INFO)

    def wrapper(*args, **kwargs):
        logging.info(
            "Ran with args: {}".format(args, kwargs))
        return orig_func(*args, **kwargs)

    return wrapper


# decorating
@my_logger
def display_info(name, age):
    print("display_info ran with parameters ({}, {})".format(
        name, age))


if __name__ == '__main__':
    # Without decorator notation
    # decorated_display = decorator_function(display)
    # decorated_display()

    # Using decorator
    display()
    display_info("John", 24)
    display_info("Mary", 33)