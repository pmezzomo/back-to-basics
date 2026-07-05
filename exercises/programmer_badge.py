"""
My Programmer Badge
Ask for the name, age, favorite language, and an emoji that represents the person.
Then, display everything formatted like a tech event badge.
"""
import os

name = input("What is your name: ")
age = input("What is your age: ")
favorite_language = input("Favorite Language: ")

os.system('clear')

print("-------------")
print("******************************")
print()
print("💻Dev Badge")
print(f'Name: {name}')
print(f'Age: {age}')
print(f'Favorite Language: {favorite_language}')
print()
print("******************************")