import os

os.chdir("C:/Users/Benjamin LOISON/Desktop/BensFolder/School/CPGE/Fenelon/MPSI/IPT/19/3/27/")

file = open("ascii.txt", "wb")
file.write(bytes(range(256)))
file.close()

# from internet import codecs

#file = codecs.open("utf8.txt", "wb", "utf-8")
#file.write(bytes(range(256)))
#file.close()

b'P5\r\n'[-1] # 10
print(bytes([110]))

# i did it personnaly
file = open("utf8.txt", "wb")
for el in range(2**15-1):
    file.write(chr(el).encode('utf_8'))
file.close()

# max 2**21 - 1 (4 octets max)

print(bin(226))
print(bin(130))
print(bin(172))
print(int(0b0010000010101100))
# 11100010 10000010 10101100

print(ord('é'))
print(bin(233)) # 2 octet car > (large ?) 128
110 00011 10 101001 # code d'abord la queue

int(0b11000011)
int(0b10101001)

# savoir pleinement justfié le félicité bugé @Â ..