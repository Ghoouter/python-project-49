import random

import prompt

from brain_games.cli import welcome_user
from brain_games.scripts.brain_games import main

main()
welcome_user()
print('Answer "yes" if the number is even, otherwise answer "no".')


def even_or_not():
	questions = [random.randint(1, 20) for _ in range(3)]
	for question in questions:
		print(f'Question: {question}')
		ans = prompt.string('Your answer: ')
		if ((question % 2 == 0 and ans == 'yes')
				or (question % 2 != 0 and ans == 'no')):
			print('Correct!')
			continue
		else:
			cor_ans = 'yes' if question % 2 == 0 else 'no'
			print(f"'{ans}' is wrong answer ;(. Correct answer was {cor_ans}.")
			print(f"Let's try again, !")
			break
	else:
		print("Congratulations!")