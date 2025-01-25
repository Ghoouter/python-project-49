import random

import prompt

from brain_games.cli import welcome_user
from brain_games.scripts.brain_games import main

main()
welcome_user()
print("What is the result of the expression?")


def calc():
	operators = ['+', '-', '*']
	questions = [f'{random.randint(1, 20)} {random.choice(operators)} {random.randint(1, 20)}' for _ in range(3)]
	for question in questions:
		print(f'Question: {question}')
		ans = prompt.string('Your answer: ')
		cor_ans = eval(question)
		if cor_ans == int(ans):
			print('Correct!')
			continue
		else:
			print(f"'{ans}' is wrong answer ;(. Correct answer was {cor_ans}.")
			print("Let's try again, !")
			break
	else:
		print('Congratulations!')