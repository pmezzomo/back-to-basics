"""
Mad Libs
Ask the user for 6 words and build a funny story with them.
"""

place = input("Name a place: ")
person = input("Name a famous person: ")
obj = input("Name an object: ")
color = input("Name a color: ")
verb = input("Name a verb (action): ")
number = input("Name a number: ")

print()
print("--- Your story ---")
print()
print(f"One day, {person} decided to visit {place} carrying a {color} {obj}.")
print(f"Everyone there started to {verb} when they saw it.")
print(f"In just {number} minutes, the whole city knew about it.")
print("And that's how the legend began. 🌟😂")
