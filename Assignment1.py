# Question#1
print("Twinkle, twinkle, little star,\n \tHow I wonder what you are!\n \t\tUp above the world so high,\n \t\tLike a diamond in the sky.\nTwinkle, twinkle, little star,\n \tHow I wonder what you are!")

# Question#2

import sys
print(sys.version)

# Question #3
import datetime
current = datetime.datetime.now()
print ("Current date and time : ",current.strftime("%d-%m-%Y %H:%M:%S"))

# Question#4

radius=float(input("Enter redius of the circle: "))
r2= radius**2
Area=3.14*r2
print ("Area of the given circle is ",Area)


#Question #5

FirstName=str(input("Enter first name: "));
LastName=str(input("Enter last name: "));
print(LastName,FirstName)

# Question#6

num1=float(input("Enter first value: "))
num2=float(input("Enter second value: "))
result=num1+num2
print("The sum of both the values is: ",result)