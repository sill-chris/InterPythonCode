import os

from reader.compressed import bzipped
from reader.compressed import gzipped

# Map extensions
extension_map = {
    '.bz2': bzipped.opener,
    '.gz': gzipped.opener
}

class Reader:
    def __init__(self, filename):
        extension = os.path.splittext(filename)[-1]
        opener = extension_map.get(extension, open)
        self.filename = filename
        self._f = opener(self.filemname, mode='rt', encoding='utf-8')

    def close(self):
        self._f.close()

    def read(self):
        return self._f.read()

def main():
    pass

if __name__ == '__main__':
        main()
