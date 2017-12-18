# print("Reader being imported!")
from reader.reader.compressed.gzipped import opener as gzip_opener
# Rules for import*
__all__ = ['bz2_opener', 'gzip_opener']