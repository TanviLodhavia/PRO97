import random
list=[1, 2, 3, 4, 5, 6, 7, 8, 9]
number=random.choice(list)
chance=0
g = input("Enter Your Guess...")
guess=int(g)

while chance < 5:
    if number==guess:
        print("You win!")
        break
    else:
        g = input("Wrong answer, try again...")
        guess=int(g)
    chance+=1
    if not chance < 5:
        print("YOU LOSE!!! The number is ", number)

