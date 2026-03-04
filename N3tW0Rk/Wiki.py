a = 100
b = format(a,'08b')
c = a.to_bytes(1,byteorder = 'big')
print(c)

