"""
Guess the Color
Create a program that simulates a magic trick!
Ask the person to think of a color and "guess" it at the end.
"""
import random

print("Welcome to 'Guess the Color'! Think of a color...")
input()

print("I'm reading your mind... 🧐")
input()

colors = ['blue', 'red', 'yellow', 'purple', 'green']
user_color = random.choice(colors)
print(f"The color you thought of was {user_color}! 🎩✨😎")
