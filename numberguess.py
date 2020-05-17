import random

comp_guess=random.randint(1,10)

limit=0
score=0

while limit<3:
    try:
        user_guess=int(input("enter a guess between 1 to 10:"))
        if (user_guess>10 or user_guess<1):
            print("invalid input")
            limit=limit
    except:
        print("enter a value in the range")

    if user_guess==comp_guess:

        if limit==0:
            score+=15
            break

        elif limit==1:
            score+=10
            break

        elif limit==2:
            score+=5
            break

    elif (comp_guess>user_guess):
        print("Your guess is lower than the comp_guess")


    elif (comp_guess<user_guess):
        print("Your guess is greater than the comp_guess")

    else:
        score=score

    limit+=1

if limit>2:
    print("Game Over")
    print("My number was:", format(comp_guess))

else:
    print("Congo! Your score is", format(score))
