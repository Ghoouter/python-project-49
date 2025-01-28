from random import randint


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_NUMBER = 1
MAX_NUMBER = 100


def is_even():
	flag = False
	if num % 2 == 0:
		flag = True
	return flag


def make_question_and_correct_answer():
	number = randint(MIN_NUMBER, MAX_NUMBER)
	question = str(number)
	if is_even(number):
		correct_answer = 'yes'
	else:
		correct_answer = 'no'
	return question, correct_answer