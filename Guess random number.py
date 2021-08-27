import random
import math

lower = int(input("enter lower range number: "))

upper = int(input("enter upper range number: "))

random_number = random.randint(lower, upper)

print("\n\tyou have only ", round(math.log(upper-lower+1, 2)), "chances to guess the integer!\n")

count = 0

while count < math.log(upper-lower+1, 2):

    guessed_number = int(input("guess a number: "))
    count += 1

    if guessed_number==random_number:
        print(f"Congratulations!, u guessed it in {count} attempt only")

        break

    elif guessed_number>random_number:
        print("u guessed it wrong, it's larger than guessed number")

    elif guessed_number<random_number:
        print("u guessed it wrong, it's smaller than guessed number")