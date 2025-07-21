import zlib

data = b"hello world \n" * 10

compressed = zlib.compress(data)
print(len(compressed))
print(zlib.decompress(compressed))