# a random number is generated which the user has to guess
# too high, too low, thats it! will be given to help

import random

random_number = random.randint(0,100)

guess = -1 
while guess != random_number:
    guess = int(input("Enter your guess: "))
    if random_number > guess:
        print('Too low!')
    if random_number < guess:
        print('Too high!')
print(f"That's it! The magic number is {random_number}")

        
