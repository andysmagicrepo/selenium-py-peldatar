x = 97
for i in range(8):
    print(chr(x), x, chr(x+1), (x+1), chr(x+2), (x+2))
#   print(chr(x), hex(x), chr(x + 1), hex(x + 1), chr(x + 2), hex(x + 2))
    x += 3
print(chr(x), x, chr(x + 1), (x + 1))