"""
Secret Number
Choose a fixed number and ask the user to try guessing it until they get it right (for real).
"""

number = 27
attempts = 0

while True:
    user_number = int(input('Guess the number I chose between 20 and 30: '))
    attempts += 1
    if user_number != number:
        print("Wrong, try again!")
    else:
        print(f'You got it in {attempts} attempt(s)!')
        break
