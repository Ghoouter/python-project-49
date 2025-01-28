import math
from random import randint

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MIN_NUMBER = 1
MAX_NUMBER = 65


def is_prime(number):
	if number < 2:
		return False
	for d in range(2, int(math.sqrt(number)) + 1):
		if number % d == 0:
			return False
	return True


def make_question_and_correct_answer():
	number = randint(MIN_NUMBER, MAX_NUMBER)
	question = str(number)
	if is_prime(number):
		correct_answer = 'yes'
	else:
		correct_answer = 'no'
	return question, correct_answer