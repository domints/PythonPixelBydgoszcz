
s = 'f8 80 f8 00 f8 00 f8 00 f8 00 f8 f8 f8 80 00 f8 00 f8 00 80 78 00 80 78 f8 80 f8 00 f8 00 f8 00 f8 00 f8 f8 f8 80 00 f8 00 f8 00 80 78 00 80 78'
bs = s.split()

res = ''

for b in bs:
    sval = bin(int(b, 16))[2:].zfill(8)
    res += '0'
    res += sval
    res += '1'

print(res)