## Classes

# with a class it's possible to create custom objects
# with his own "special-powers"

class SimplePerson(object):
    pass
    
p = SimplePerson()

print p

p.firstName = "Fred"
p.familyName = "Flinstone"

print p.firstName
    
# add methods

class Person(object):
    
    def __init__(self):
        self.firstName = ""
        self.familyName = ""
        self.street = ""
        
    def fullName(self):
        return self.firstName + " " + self.familyName
    
    def info(self):
        return "%s\n%s" %(self.fullName(), self.street)
    
    def __len__(self):
        return len(self.firstName) + len(self.familyName)
    
p = Person()

print p.fullName()

p.firstName = "Fred"

print p.fullName()

p.familyName = "Flinstone"

print p.fullName()

p.street = "Road 4"
print p.info()
print len(p)


# inhert objects
class TypeDesigner(Person):
    
    def __init__(self):
        super(TypeDesigner, self).__init__()
        self.designed = []
    
    def info(self):
        info = super(TypeDesigner, self).info()
        return "%s\n%s" %(info, ", ".join(self.designed))
        
td = TypeDesigner()
td.firstName = "Fred"
td.familyName ="Flinstone"
td.street = "Road 4"

td.designed.append("Stone")
td.designed.append("Clay")

print td.info()

    
    
        
        