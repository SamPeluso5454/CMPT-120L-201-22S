class Person:
    def __init__(self, weight: int, height: int, name: str):
        self.weight = weight
        self.height = height
        self.name = name

    def who_is_this(self):
        print("This person's name is " + self.name)
        print("This person's weight is " + str(self.weight) + " pounds")
        print("This person's height is " + str(self.height) + " inches")
    