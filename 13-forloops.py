# forloops - Execute a block of code a fixed number of times
#            you can iterate over a range , string , seequence

# iterate in normal
for x in range (1,10):
    print(x)

#iterate in reverse
for x in reversed(range(1,11)):
    print(x)

print("Happy New Year..!!")

# iterating the number by 3 steps , third parameter in the range is for step
for x in range(1,10,3 ):
    print(x)

print("Now i terate a above loop with a step of two..!!")

#continue & break
# in for loop if we want to skip one iteration we needs to use the keyword continue
#  in for loop if we want to close the loop function and executes the next line we needs to use break

for x in range (1,15):

    # lets skip the iteration if X == 6
    if x == 6:
        continue
    #  Lets break the loop if X == 9
    elif x == 9:
        break
    else:
        print(x)

