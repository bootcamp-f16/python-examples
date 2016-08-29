#Capitalize str

str = "hello world!"
print "str. capitalize() : ", str.capitalize()

# true/false/not true

x = 5
y = 10
z = 15

print x == 5
print x == 5 and y == 9
print z == 10 and x == 4
print  not x == 4 and y == 10 

### Date and Time

from datetime import datetime
now = datetime.now()

print '%s:%s:%s' % (now.hour, now.minute, now.second)
