import random
print("----------------------------------------------------------------------------------")
print("                               GUESS THE NUMBER")
print("----------------------------------------------------------------------------------")

cguess = random.randint(1,101)
uname = input("What is your name?")
iuguess = -1

while(1):
    uguess=input("Hi! "+uname+", Guess an integer between 1 to 100.")
    iuguess= int(uguess)
    if cguess>iuguess:
        print("hey "+uname+", your guess was a bit low!")
    elif cguess<iuguess:
        print("hey "+uname+", your guess was a bit high!")
    else:
        print("Congrats! "+uname+", Your guess was right!")
        break