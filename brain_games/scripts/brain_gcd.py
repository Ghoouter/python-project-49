import random

import prompt

from brain_games.cli import welcome_user
from brain_games.scripts.brain_games import main

main()
welcome_user()
print('Find the greatest common divisor of given numbers.')


def gcd(m, n):
	while m != n:
		if m > n:
			m = m - n
		else:
			n = n - m
	return n


def game_gcd():
	questions = [(random.randint(1, 30), random.randint(1, 30)) for _ in range(3)]
	for question in questions:
		print(f'Question: {question[0]} {question[1]}')
		ans = prompt.string('Your answer: ')
		cor_ans = gcd(int(question[0]), int(question[1]))
		if int(ans) == cor_ans:
			print('Correct!')
			continue
		else:
			print(f"'{ans}' is wrong answer ;(. Correct answer was {cor_ans}.")
			print("Let's try again, !")
			break
	else:
		print('Congratulations!')