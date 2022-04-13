#Isaiah Lawlor - Lab Three

#if statement 
I_am_hungry = True
if I_am_hungry:
    print("I am going to the dining hall.")

#else statement
I_am_hungry = False
if I_am_hungry:
    print("I am going to the dining hall.")
else:
    print("I am going to the library to study.")

#Elif statement
I_am_hungry = False
It_is_the_weekend = True
I_do_not_have_big_exam_soon = True
if I_am_hungry:
    print("I am going to the dining hall.")
elif I_do_not_have_big_exam_soon and It_is_the_weekend:
    print("I am going with friends to the game")
else:
    print("I am going to the library to study.")

#for Loop 
for value in range(0,10):
    print(value)

#for Loop with colors
arr =['Blue', 'Yellow','Red','Green','Purple','Magenta','Lilac']

for value in range(7):
    print(arr[value])
    print(value)

#While Loop
Shaq_free_throw_result = 5
position = 0
while position != Shaq_free_throw_result:
    print("Shaq missed the FT")
    position += 1
print("Shaq made the FT")

#Functions
a=20+17
b=2+8
c=250.00+49.99
print(a)
print(b)
print(c)
print(c>b)

#Odd or Even
from random import randint
from unicodedata import name
secret_number=randint(1,10)
position = 1

while position!= secret_number:
    if (position%2)==0:
        print(format(position), "is even")
    else:
        print(format(position),"is odd")
    position += 1
print("Excercise complete")

#Odd or Even (v2)
num= int(input("Enter a number: "))
if (num%2)==0:
    print(format(num), "is Even")
else:
    print(format(num), "is Odd")

#Objects
class Dog(object):
    def __init__(self,name,height,weight,breed:str):
        self.name=name
        self.height=height
        self.weight=weight
        self.breed=breed

    def info(self):
        print("Name: ",self.name)
        print("Weight: ", str(self.weight)+"Pounds")
        print("Height: ",str(self.height)+"inches")
        print("Breed: ", self.breed)

if __name__ == "__main__":
    Spike = Dog("Maple",34,75,"Golden Retreiver")
    Spike.info()
    print(Spike.name)