a = ["green", "blue", "white", "black"]
b = a
c = list(a)
d = c
a[3] = "red"
c[2] = a[1]
b = a[1:3]
b[1] = c[2]
print a
print b
print c
print d
s