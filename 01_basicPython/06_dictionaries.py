## Dictionaries 

# A dictionary is a keyword assigned collections of objects
# keyword can be a string, number or an other kind of object

# create a dictionary with curly brackets
myDict = {"aKeyWord" : 6, "anOtherKeyWord" : "Hello World"}
print myDict

# retrive the value based on a keyword
# if the keyword is not a valid keyword it will raise an KeyWord error
print myDict["aKeyWord"]

# retrive the value based on a keyword with a fallback
print myDict.get("keyWordNotInTheDict", "myFallbackValue")

# add/change a keyword value
myDict["aKeyWord"] = 9
myDict["newKeyWord"] = "newValue"

# get all keywords from the dictionary
print myDict.keys()
# get all values from the dictionary
print myDict.values()
# get a combined list of keywords and values from the dictionary
print myDict.items()