is_student = False

if is_student:
    print("you are student")
else:
    print("you are not a student")

for_sale = False

if for_sale:
    print("yes this item is for sale")
else :
    print("not available for sale")

# check if he is eligible for vote

Age = input("enter your age")

if int(Age) > 18 and int(Age) < 40 :
    print("eligible for vote")
elif int(Age) > 40 :
    print("eligible for Vetran Voting")
else:
    print("Not eligible for voting")