i=100
print("guess no. ")
guess=8

while(True):
    if guess !=  0 :
        print("enter your guess")
        x=int(input())
        if x>i:
            print("greater")
        elif x<i:
            print("less")
        else:
            print("yes")
            break
        guess=guess-1
        print(guess,"guesses left")
    else:
        print("guesses ended")


