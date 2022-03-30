# Initialize an instance of the following class. Use a variable to store the object and then call the info function to print out the attributes.
class Dog(object):
    def __init__(self, name, height, weight, breed):
        self.name = name
        self.height = height
        self.weight = weight
        self.breed = breed

    def info(self):
        print("Name:", self.name)
        print("Weight:", str(self.weight) + " Pounds")
        print("Height:", str(self.height) + " Inches")
        print("Breed:", self.breed)
    