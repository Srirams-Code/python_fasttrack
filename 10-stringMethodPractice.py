# validate your username
#1. username should not be more than 12 letters
#2. username must not contain spaces
#3. username must not contain digits

user_name = input("enter your Name")

if( len(user_name)>12 or user_name.isspace()== True or not user_name.isalpha()):
    print("user name is invalid")
else : 
    print(f"hey {user_name} ..!!")

