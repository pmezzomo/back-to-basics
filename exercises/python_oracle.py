"""
Python Oracle
An assistant that answers programming questions based on the topic you type.
"""

topic = input("Ask the Oracle about a programming topic (e.g. variables, loops, functions, lists, recursion): ").lower()

match topic:
    case "variables":
        print("🔮 Variables store data in memory. In Python, you don't need to declare a type — just assign a value: x = 10")
    case "loops":
        print("🔮 Loops repeat a block of code. Use 'for' to iterate over a sequence, and 'while' to repeat while a condition is true.")
    case "functions":
        print("🔮 Functions are reusable blocks of code. Define them with 'def', give them a name, and call them whenever needed.")
    case "lists":
        print("🔮 Lists store multiple values in order. You can access items by index, add with .append(), and remove with .remove().")
    case "recursion":
        print("🔮 Recursion is when a function calls itself. Always define a base case to avoid infinite loops!")
    case _:
        print("🔮 Hmm... the Oracle is still learning about that. Try: variables, loops, functions, lists, or recursion.")
