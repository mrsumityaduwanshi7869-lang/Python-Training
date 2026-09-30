
## type 1

n1 = 0o17
n2 = 0x00AF
n3 = 0b110101
n = int(n1)
print("Octal 17 = ",n)

n = int(n2)
print("Hexa 00AF = ",n)

n = int(n3)
print("Binary 110101 = ",n)


## type 2

s1 = "0o17"
s2 = "0x00AF"
s3 = "0b110101"

n = int(s1,8)
print("Octal 17 = ",n)

n = int(s2,16)
print("Hexa 00AF = ",n)

n = int(s3,2)
print("Binary 110101 = ",n)


## type 3

t1 = oct(0o17)
t2 = hex(0x00AF)
t3 = bin(0b110101)

print("Octal 17 = ",t1)
print("Hexa 00AF = ",t2)
print("Binary 110101 = ",t3)
