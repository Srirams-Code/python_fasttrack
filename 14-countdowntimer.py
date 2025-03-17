import time

# sleep is used to wait/ delay the program from running for mentioned amount of time
# time.sleep(3)
# print("3 seconds over")

# getting input and execute sleep

# delayTime = int(input("How long you want me to delay/ wait the program execution ? "))
# time.sleep(delayTime)
# print(f"this line of program getting execute after {delayTime} secs")

# # Countdown Program 

# for x in range (delayTime, 0 , -1):
#     print(x)
#     time.sleep(1)

# print(f"Times's Up")

# countdown timer

cdDuration = int(input("How many sec you want to have count down "))

for x in range (cdDuration , 0 , -1):
    sec = x % 60
    min = int(x/60) % 60
    print(f"00:{min:02}:{sec:02}")
    time.sleep(1)

