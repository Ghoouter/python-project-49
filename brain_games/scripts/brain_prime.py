import random

import prompt

from brain_games.cli import welcome_user
from brain_games.scripts.brain_games import main

main()
welcome_user()
print('Answer "yes" if given number is prime. Otherwise answer "no".')


def is_prime(n):
    d = 2
    while d * d <= n and n % d != 0:
        d += 1
    return d * d > n


def prime_or_not():
	questions = [random.randint(1, 20) for _ in range(3)]
	for question in questions:
		print(f'Question: {question}')
		ans = prompt.string('Your answer: ')
		if ((is_prime(question) and ans == 'yes')
				or (not is_prime(question) and ans == 'no')):
			print('Correct!')
			continue
		else:
			cor_ans = 'yes' if is_prime(question) else 'no'
			print(f"'{ans}' is wrong answer ;(. Correct answer was {cor_ans}.")
			print("Let's try again, !")
			break
	else:
		print("Congratulations!")