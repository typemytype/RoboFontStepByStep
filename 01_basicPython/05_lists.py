## Lists

# a list is always ordered 
myList = [1, 2, 3, 4]
print myList

# can contain a mixture of different sort of objects
myList = ["hello", 1, 2, 1, 3, "world"]

print myList
print myList[0]         # get the first item of the list
print myList[1]         # get the second item of the list

print myList[-1]        # get the last item of the list
print myList[-2]        # get the second last item of the list

# count
print myList.count(1)   # returns the number of times the item
                        # appears in the list 

# append an item
myList.append(865)      # add an item to the end of the list

# insert an item at a specific index
myList.insert(1, "Welcome")

# lenght of a list
print len(myList)       # count how many items are in the list
print myList

# strings also act as list
myString = "hello world"
print myString[0]

# slicing
print myList[2:6]       # subset the list from index to index

# creating lists
print range(10)         # a list of numbers going from 0 to 10
print range(2, 10)      # a list of numbers going from 2 to 10
print range(2, 10, 3)   # a list of numbers going from 2 to 10 in steps of 3
