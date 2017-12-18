import bz2
import sys

# Do not include ()
opener = bz2.open


if __name__ == '__main__':
    f = bz2.open(sys.argv[1], mode='rt', encoding='utf-8')
    f.write(' '.join(sys.argv[2:]))
    f.close()