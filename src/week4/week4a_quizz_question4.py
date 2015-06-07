x = range(5)
y = x
x = [0, 1, 10, 3, 4]
print "x,y=", x, y

x = range(5)
y = x
y[-3] = 10
print "x,y=", x, y

x = range(5)
x = y
x[2] = 10
print "x,y=", x, y

x = range(5)
y = x
x[2] = 10
print "x,y=", x, y

x = range(5)
y = x
y = [0, 1, 10, 3, 4]
print "x,y=", x, y
