"""
Create a program that asks the user for 6 words (e.g., place, famous person, object, color, verb, number) 
and puts together a short, funny story using them.
"""

print("Welcome to Madlib")

place = input("Name a place: ")
person = input("Name a famous person: ")
obj = input("Name an object: ")
color = input("Name a color: ")
verb = input("Name a verb (action): ")
number = input("A number: ")


print("One day " + person + " decided to visit " + place + " carrying a "+ color + " " + obj +" Everyone there ")
print("started to "+ verb + " when they saw it. In just " + number + " minutes, the whole city knew about it.")
print("And that's how the legend began.🌟😂")