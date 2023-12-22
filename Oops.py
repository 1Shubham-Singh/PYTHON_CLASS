
class Name:
 
    # class attribute
    attr1 = "Soham"
 
    # Instance attribute
    def __init__(self, name):
        self.name = name
 
# Driver code
# Object instantiation
Soham = Name("Soham")
Rohan = Name("Rohan")
 
# Accessing class attributes
print("He is a {}".format(Soham.__class__.attr1))
print("He is also a {}".format(Rohan.__class__.attr1))
 
# Accessing instance attributes
print("My name is {}".format(Soham.name))
print("My name is {}".format(Rohan.name))

