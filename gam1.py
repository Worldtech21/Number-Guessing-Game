import math 
import random

diff = 0
while diff<10:
    lower = int(input("Enter the Lower Bound:-"))
    upper = int(input("Enter the Upper Bound:-"))
    diff = upper - lower
    if diff<10:
        print("Minimum range is 10! ")


print("You have ", round(math.log(upper-lower+1, 2)), " chances to get it right")

Jack_Pot = random.randint(lower, upper )

count = 0 

while count<(math.log(upper-lower+1, 2)):
    guess  = int(input("Enter your guess"))
    if guess == Jack_Pot:
        print("Bingo! Ye got it right!👌🥰🫡🥳")
        quit()
    elif guess<Jack_Pot:
        print("Wrong ❌ 😂 (🤫Try a bigger number")
    else:
        print("Wrong ❌ 😂 (🤫Try a smaller number")

print("Alas My Friend😋\nYour Loss❤️‍🩹\nBetter Luck Next Time💕") 
