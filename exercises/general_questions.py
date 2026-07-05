"""
Q&A Quiz
Create a quiz game with scoring.
"""
questions = [
    ["What is the capital of France?", "paris"],
    ["Which planet is known as the Red Planet?", "mars"],
    ["How many sides does a hexagon have?", "6"],
]

score = 0

for question in questions:
    answer = input(f"{question[0]} ").lower()
    if answer == question[1]:
        print("Correct! ✅")
        score += 1
    else:
        print(f"Wrong! The correct answer was: {question[1]} ❌")

print(f"\nYou scored {score} out of {len(questions)}!")
