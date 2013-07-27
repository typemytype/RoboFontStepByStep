## conditional statements

# setup some variables
a = 5
b = 10

# is equal
print a == b

# is not equal
print a != b

# greater than
print a > b

# greater than or equal
print a >= b

# is less than
print a < b

# is less than or equal
print a <= b


# make conditional descisions 
# be carefull with the indetentation

if a < b:
    print "a is greater than b"

# if then else that    
if a > b:
    print "a is less than b"
else:
    print "a is greater than b"
    

# if that else if aht else that
if a > b:
    print "a is less than b"
elif a == b:
    print "a is equal to b"
else:
    print "a is greater than b"
    
# combine conditions with boolean operators
# and or not
if a > b and a == 5:
    print "a is greater than b and a is equal to 5"

elif a > b or a == 5:
    print "a is greater than b or a is equal to 5"

