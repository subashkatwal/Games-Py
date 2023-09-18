import random
jackpot = random.randint(1, 100)
guess = int(input("Guess the number between 1 to 100: "))
counter = 1

while guess != jackpot:
    if guess < jackpot:
        print("Guess Higher")
    else:
        print("Guess Lower")
    guess = int(input("Guess the number between 1 to 100: "))
    counter += 1

print("COngratulations you guessed it right!")
print("You took ",counter,"attempts")