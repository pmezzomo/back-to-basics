questions = [ ['Does your animal like bananas', 'monkey'] ]

while True:
    print('Think of an animal...')

    guessed = False
    for question in questions:
        answer = input(f'{question[0]} (y/n): ')
        if answer.lower() == 'y':
            print(f'You thought of a {question[1]}!')
            guessed = True
            break

    if not guessed:
        animal = input('I give up! What animal were you thinking of? ')
        new_question = input('What question would you ask to tell that animal apart? ')

        questions.append([ new_question, animal])

        answer = input('Want to play again? (y/n): ')
        if answer.lower() != 'y':
            print('Ok! It was fun playing with you!')
            break