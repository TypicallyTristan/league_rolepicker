import time
import random


random_int = random.randint(0,4)


Roles = ["Top", "Jungle", "Mid", "Bottom", "Support"]

print("Hey there!")

time.sleep(1)
print("Hey! Hold on!! Don't click find match yet!")

time.sleep(2.2)
print("Now, that i've got your attention...")

time.sleep(2.5)
print("Did you wanna play a little roulette?")

time.sleep(1.5)
print("Waddya say?")

while True:
    time.sleep(1)
    answer = input("yes or no: ").lower()
    if answer in ("n", "no"):
        time.sleep(0.5)
        print("awww that's too bad")
        exit(1)
    elif answer in ("y", "yes"):
        ("Great! I'll randomly pick the role you'll be picking next match!")
        break
    else:time.sleep(1) 
    print("Did league fry your brain..? Let's try this again.") # in case of invalid input


time.sleep(1)
print("Great! You already know the roles so lets just get right into it.")