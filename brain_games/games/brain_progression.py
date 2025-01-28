from random import randint
from tarfile import LENGTH_PREFIX

DESCRIPTION = 'What number is missing in the progression?'
MIN_LENGTH = 5
MAX_LENGTH = 10
LENGTH = randint(MIN_LENGTH, MAX_LENGTH)
START_MIN, START_MAX = 1, 10
STEP_MIN, STEP_MAX = 1, 5


def hide_element(progression):
	hidden_index = randint(0, len(progression) - 1)
	hidden_element = progression[hidden_index]
	progression[hidden_index] = ".."
	return hidden_element, progression


def generate_progression(length, start, step):
	progression = [start + i * step for i in range(length)]
	return progression


def make_question_and_correct_answer():
	length = randint(MIN_LENGTH, MAX_LENGTH)
	start = randint(START_MIN, START_MAX)
	step = randint(STEP_MIN, STEP_MAX)
	progression = generate_progression(length, start, step)
	correct_answer, progression = hide_element(progression)
	question = ' '.join(map(str, progression))
	return question, correct_answer