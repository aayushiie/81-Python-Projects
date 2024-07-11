#Date: July 4, 2024
#Project 1: Bagels 
# In Bagels, a deductive logic game, you must guess a secret three-digit number based on clues. The game offers one of the following hints in response to your guess: “Pico” when your guess has a correct digit in the wrong place, “Fermi” when your guess has a correct digit in the correct place, and “Bagels” if your guess has no correct digits. You have 10 tries to guess the secret number.

import random

Max_guess = 10
Max_digit = 3

def main():

    print('''
Instructions: Guess the digits of a randomthree digit number. ik it's frustrating buthey, let's not waste my efforts.
        
So here are the rules:
Rule 1: You get 10 attempts which is not alot 'cause it still leaves the probability ofguessing it right to 0.011 or 1.11%(umm...)
        
And Rule 2:
When I say:      That means:
Pico             correct digit at wrong place
Fermi            correct digit at correct place
Bagels           wrong digit at wrong place

That's it. Those are the rules.
Let's start now!
    ''')


    #random number from int to str to list
    actualNumber_int = random.randrange(100,999)
    actualNumber_str = str(actualNumber_int)
    actualNumber = [int(y) for y in str(actualNumber_str)]

    print(actualNumber) #delete this later

    while True:
        i = 1
        while(i <= Max_guess):
            number = input(f"Guess #{i}:\n")

            #converting the number to string and then to list
            str(number)
            array = [int(x) for x in str(number)]
        
            if(array[0] == 0 or len(array)>Max_digit or len(array)< Max_digit):
                print("Something went wrong 'cause the format was not correct.\nRestarting...")
                break

            clues = compare(array, actualNumber)
            print(clues)

            i += 1

            if array == actualNumber:
                break

            if i == Max_guess+1:
                print(f"You ran out of guesses. The answer was {actualNumber_int}")

        input("Wanna play again? (yes or no)")
        if input != ('y' or 'Y' or 'yes' or 'Yes'):
            break

    print("Thanks for playing <3")


def compare(array, actualNumber):

    if array == actualNumber:
        print("Wow you won! What are the odds!")
    clues = [] 

    for i in range(len(array)):
        if array[i] == actualNumber[i]:
            clues.append('Fermi')
        elif array[i] in actualNumber:
            clues.append('Pico')
        
    if len(clues) == 0:
        return 'Bagels'
    else:
        clues.sort()
        return ' '.join(clues)
        
if __name__ == '__main__':
    main()
            

