import os, gzip

def read_file(fname, compress=False):
    f = gzip.GzipFile(fname, 'rb') if compress else open(fname, 'rb')
    try:
        data = f.read()
    finally:
        f.close()
    return data
  
def write_file(data, fname, compress=True):
    #print(os.getcwd())

    f = gzip.GzipFile(fname, 'wb') if compress else open(fname, 'wb')
    try:
        f.write(data)
    finally:
        f.close()

data = read_file('hey.txt')
print(data)

data = read_file('hey.gz', True)
print(data)

write_file(b'This is a hello string', 'hello.txt', False)
write_file(b'This is a hello string in compress format', 'hello.txt.gz')