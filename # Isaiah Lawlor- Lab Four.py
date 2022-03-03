# Isaiah Lawlor- Lab Four
# Swap Case
from cmath import sqrt
from re import X


string = "upper LOWER big SMALL bOtH"
print('Original String: ',string)
print('Updated String: ', string.swapcase())

# Padding Strings
string2 = "Fat"
print('Orginal String: ', string2)
string3 = string2.rjust(7, '-')
string4 = string3.ljust(11,'-')
print('Updated String:', string4)

# Partitioning Text
statement = "FAX = I need a partition to sperate me and my roomate when his gf is over"
truth = statement.partition("partition")
print('Result:', truth)

# Function to Raise Number to Power of Input
print('Enter a number to be squared: ')
z = int(input())
y = pow(2,z)
print('Your Answer is: ',y)

# List Interprettor
print('Pats beat the Bucs 31-28, but how many FGs were scored? ')
List1= [3,7,6,3,7,2,3]
score= List1.count(3)
print('Number of Field Goals Scored:',score)

#Slope Formula
def slope(x1,y1,x2,y2):
    return (float)(y2-y1)/(x2-x1)
x1 = 8
y1 = 5
x2 = 7
y2 = 2
print("The slope is: ",slope(x1,y1,x2,y2))

def distance(x1,y1,x2,y2):
    
    return (float)(((y2-y1)**2)+((x2-x1)**2))**.5
x1 = 10
y1 = 5
x2 = 7
y2 = 2
print("The Distance is: ",distance(x1,y1,x2,y2))