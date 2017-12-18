import sys
import reader

r = reader.Reader(sys.arg[1])
try:
    print(r.read())
finally:
    r.close()


# print("Executing __main__.py with name{}".format(__name__))