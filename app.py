# a dictionary that stores questions and answers
#a variable that tracks the score of the player
# loop through the dict using key value paairs
# display each question to the user and allow them to answer
#tell them if they are right or wrong
# show the final result

quiz = {
    'question1': {
        'question': 'What is the capital of France',
        'answer': 'Paris'
    },
    'question2': {
        'question': 'What is the capital of Germany',
        'answer': 'Berlin'
    },
    'question3': {
        'question': 'What is the capital of Italy',
        'answer': 'Rome'
    },
    'question4': {
        'question': 'What is the capital of Spain',
        'answer': 'Madrid'
    },
    'question5': {
        'question': 'What is the capital of Portugal',
        'answer': 'Lisbon'
    },
    'question6': {
        'question': 'What is the capital of switzerland',
        'answer': 'Bern'
    },
    'question7': {
        'question': 'What is the capital of Austria',
        'answer': 'Vienna'
    }
}

score = 0

for key, value in quiz.items():
    print(value['question'])
    answer = input('Answer? ')

    if answer.lower() == value['answer'].lower():
        print('correct')
        score += 1
        print(f'Your score is {score}')
        print()

    else:
        print('Wrong')
        print(f'The answer is: {value['answer']}')
        print(f'Your score is {score}')
        print()

print(f'You got {score} out of 7 correctly')
print(f'Your percentage {int((score/7)*100)}% ')