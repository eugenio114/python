def tail(file, n=1, bs=1024):
    with open(file) as f:
        f.seek(0,2)
        l = 1-f.read(1).count('\n')
        B = f.tell()
        while n >= l and B > 0:
                block = min(bs, B)
                B -= block
                f.seek(B, 0)
                l += f.read(block).count('\n')
        f.seek(B, 0)
        l = min(l,n)
        lines = f.readlines()[-l:]
    return lines
	
lines = tail("SampleTextFile_10kb.txt", 2)
for line in lines:
	print (line)