import time
import random


random_int = random.randint(0,4)

roles = ["Top", "Jungle", "Mid", "Bot", "Support"]

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

time.sleep(1)
print(".")
time.sleep(1)
print("..")
time.sleep(1)
print("...")


result = roles[random_int]

time.sleep(1)
print("You got", result)
if result == ("Top"):
    time.sleep(1)
    print("Have fun on your island")
elif result == ("Jungle"):
    time.sleep(1)
    print("Enjoy afk farming")
elif result == ("Mid"):
    time.sleep(1)
    print("Run it down for me :)")
elif result == ("Bot"):
    time.sleep(1)
    print("sensing a 0/3 in your future")
elif result == ("Support"):
    time.sleep(1)
    print("my support can't hit a single hook")