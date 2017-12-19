import time
from functools import wraps


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

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        logging.info(
            "Ran with args: {}".format(args, kwargs))
        return orig_func(*args, **kwargs)

    return wrapper


def my_timer(orig_func):
    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print("{} ran in: {}". format(orig_func.__name__, t2))
        return result
    return wrapper

# decorating with multiple decorators
# decorating with multiple decorators using wraps


@my_logger
@my_timer
def display_info(name, age):
    print("display_info ran with parameters ({}, {})".format(
        name, age))
    time.sleep(1)


if __name__ == '__main__':
    # Without decorator notation
    # decorated_display = decorator_function(display)
    # decorated_display()

    # Using decorator
    # display()
    # display_info("John", 24)
    display_info("Tom", 33)