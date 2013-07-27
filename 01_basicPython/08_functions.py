# Functions

# a repeated action can be bundled into a single function

def myFunction():
    print "hello"
    
myFunction()
myFunction()

# arguments can be passed along

def myMathFunction(number):
    print number * 6

myMathFunction(9)
myMathFunction(60)


# function can also return a value

def myReturningFunction(number):
    return number * 6

print myReturningFunction(9)    # prints 54
print myReturningFunction(60)   # prints 360 

# compare
print myMathFunction(60)        # will print None, 
                                # cause the function is not returning anything
