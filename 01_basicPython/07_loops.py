## Loops

# Loops over lists:
# indentations is very important
# evertying on the same indentation level will be exectuded inside the loop

print "loop over a list"
myList = ["hello", 1, 2, 1, 5]

for item in myList:
    print item 

print "loop over a string"
for char in "Hello World":
    print char

print "loop over a range of numbers:"
for i in range(10):
    print i

print "a loop in a loop:"
for x in range(10):
    for y in range(10):
        print x, y

# loop over dictionaries

myDict = {"aKeyWord" : 6, "anOtherKeyWord" : "Hello World"}

print "a loop over all keys in a dictionary"
for key in myDict.keys():
    print key
    # get the value from the dictionary based on the keyword
    print myDict[key]

print "a loop over all values in a dictionary"
for value in myDict.values():
    print value

print "a loop over all keys and values in a dictionary"
for key, value in myDict.items():
    print key, value