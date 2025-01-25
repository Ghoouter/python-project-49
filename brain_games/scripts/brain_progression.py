import random

import prompt


def brain_progression():
	questions = []

	for _ in range(3):
		start = random.randint(1, 10)
		step = random.randint(1, 10)
		length = random.randint(5, 10)
		progression = [start + step * i for i in range(length)]
		questions.append(progression)

	for question in questions:
		index_to_hidden = random.randint(0, len(question) - 1)
		hidden_value = question[index_to_hidden]
		question[index_to_hidden] = '..'
		print(f'Question: {question}')
		ans = prompt.string('Your answer: ')
		if int(ans) == hidden_value:
			print('Correct!')
			continue
		else:
			print(f"'{ans}' is wrong answer ;(. Correct answer was {hidden_value}).")
			print("Let's try again, !")
			break
	else:
		print('Congratulations!')