# while loop - Execute some codes till the conditions remains true

#example 1 

age = int(input("ENter your Age "))

while age == " " :
    print("Invalid Input")
    age = int(input("Enter your Age "))

print(f"Hi you are {age} old")

# example 2

fav_food = input("Enter your fav food ")

while not fav_food == "q" :
    print(f"your fav food is {fav_food}")
    fav_food = input("Enter your fav food ")

print("hope you enjoyed your food")