import random
randNumber = random.randint(1,100)
userGuess = None
guesses = 0

while(userGuess != randNumber):
    userGuess = int(input("Enter Your Guess :"))
    guesses +=1
    if(userGuess == randNumber):
        print("You Guessed Right!")

    else:
        if(userGuess > randNumber):
            print("You Gessed It Worng! Please Enter A Smaller Number")

        else:
            print("You Guessed it Worng! Please Enter A Larger Number")

print(f"You Guessed The Number in {guesses} guesses")
with open("hiscore.txt","r") as f:
    hiscore = int(f.read())

if(guesses<hiscore):
    print("You Have Just Broken A Score!")

    with open("hiscore.txt","w") as f:
        f.write(str(guesses))
    