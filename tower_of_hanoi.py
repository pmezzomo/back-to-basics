"""
Today, we explored the logic behind the famous Tower of Hanoi puzzle. We started by reviewing the rules and mechanics of the game, 
which involves moving disks between towers while following certain restrictions. We then discussed how to simplify the problem and apply 
recursion to create an algorithm that solves it for any number of disks. The idea is to reuse previous solutions, making it easier 
to solve more complex problems. Hope you enjoy testing the code!
🧠 Fun fact: Why is it called "Tower of Hanoi"? The Tower of Hanoi is a mathematical puzzle created in 1883 by Édouard Lucas,
a French mathematician. He invented a fictional story to make the game more interesting: In a temple in the city of Hanoi, 
capital of Vietnam, monks would be transferring disks from one tower to another following sacred rules. 
According to the legend, when they finish the task, the world will end. But don't worry — with 64 disks, 
it would take billions of years! 😅 The name "Hanoi" comes from that city, used as the setting of the invented legend that 
accompanies the challenge to this day.
"""
def move_disks(num_disks, source, target, auxiliary):
    if num_disks == 1:
        print(f"Move disk 1 from {source} to {target}")
    else:
        move_disks(num_disks - 1, source, auxiliary, target)
        print(f"Move disk {num_disks} from {source} to {target}")
        move_disks(num_disks - 1, auxiliary, target, source)

move_disks(2, "Tower 1", "Tower 3", "Tower 2")
