# nested loops - Normaly nested loops are said as loop inside of another loops
#                outer loop
#                      inner loop

# for x in range(1,4):
#     for y in range(1,10):
#         print(y , end=" ")
#     print()


# nested loops with user inputs

rows = int(input("enter number of Rows "))
cols = int(input("enter number of Cols "))

for x in range(rows):
    for y in range(cols):
        print("*" , end=" ")
    print()