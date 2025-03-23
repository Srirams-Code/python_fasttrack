# ex-1 find the area of a circle
import math

radius = float(input ("Enter the radius of a circle"))

area = math.pi * radius * radius
print(round(area,2))

# shopping cart program to find total and discount

item1 = float(input("Enter the item1 rate"))
item2 = float(input("Enter the item2 rate"))
item3 = float(input("Enter the item3 rate"))

discount = float(input("enter the discount %"))

discount_amt = discount / 100 * (item1+item2+item3)
Amt_to_pay =  ( item1 + item2 + item3 ) - discount_amt

print(Amt_to_pay)


#  find the hypotenuse of a triangle
# formula => c = a2 + b2

a = float(input("enter adjecent side"))
b = float(input("enter opposite side"))

c = pow(a,2) + pow(b,2)

print(c)