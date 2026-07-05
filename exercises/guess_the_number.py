"""
Guess the Number
Create a program that simulates a magic trick!
Ask the person to think of a number from 1 to 10 and "guess" it at the end.
"""
import random

print("Welcome to 'Guess the Number'! Think of a number between 1 and 10...")
input()

print("I'm reading your mind... 🧐")
input()

number = random.randint(1, 10)
print(f"The number you thought of was {number}! 🎩✨😎")
