import sys
import reader

r = reader.reader.Reader(sys.argv[1])
try:
    print(r.read())
finally:
    r.close()

