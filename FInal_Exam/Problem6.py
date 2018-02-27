## DO NOT MODIFY THE IMPLEMENTATION OF THE Person CLASS ##
class Person(object):
    def __init__(self, name):
        #create a person with name name
        self.name = name
        try:
            firstBlank = name.rindex(' ')
            self.lastName = name[firstBlank+1:]
        except:
            self.lastName = name
        self.age = None
    def getLastName(self):
        #return self's last name
        return self.lastName
    def setAge(self, age):
        #assumes age is an int greater than 0
        #sets self's age to age (in years)
        self.age = age
    def getAge(self):
        #assumes that self's age has been set
        #returns self's current age in years
        if self.age == None:
            raise ValueError
        return self.age
    def __lt__(self, other):
        #return True if self's name is lexicographically less
        #than other's name, and False otherwise
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName
    def __str__(self):
        #return self's name
        return self.name
        
class USResident(Person):
    """ 
    A Person who resides in the US.
    """
    def __init__(self, name, status):
        """ 
        Initializes a Person object. A USResident object inherits 
        from Person and has one additional attribute:
        status: a string, one of "citizen", "legal_resident", "illegal_resident"
        Raises a ValueError if status is not one of those 3 strings
        """
        Person.__init__(self, name)
        if status not in ["citizen", "legal_resident", "illegal_resident"] :
            raise ValueError
        else :
            self.status = status
        
    def getStatus(self):
        """
        Returns the status
        """
        return self.status
    



#Test 2 :
person2 = USResident("Mouaad ALOUANI", "legal_resident")
print("Test 2 result is : ", person2.getStatus())
if person2.getStatus() == "legal_resident" :
    test2 = "Test 2 passed"
else :
    test2 = "Test 2 failed"
    
    
print(test2)
    
#Test 1 :
try :
    person1 = USResident("Younes ALOUANI", "")
    print("Test 1 result is : ", person1.getStatus())
    if person1.getStatus() == ValueError :
        test1 = "Test 1 passed"
    else :
        test1 = "Test 1 failed"
except :
    test1 = "Test 1 failed"
print(test1)

