# logical operators = Evaluate Multiple conditions
# or - either one conditions are true
# and - Both conditions are true
# not -inverts the conditions

temp = 28
is_raining = False

# or example
if (temp > 35 or is_raining ) :
    print("outdoor event cancelled")
else :
    print("outdoor event will be held")

# and example
if(temp < 35 and is_raining == False):
   print("outdoor event will be held")
else:
    print("outdoor event cancelled")


#Conditional Expressions - writing if-else statements in single line
print("Event is ON ") if temp<35 and is_raining == False else  print("outdoor event cancelled")
print("its cold but Event is ON ") if temp<30 and is_raining == False  else  print("outdoor event cancelled")


