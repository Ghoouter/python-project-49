import prompt


MAX_ROUND = 3


def run_game(game_name):
	print("Welcome to the Brain Games!")
	user_name = prompt.string('May I have your name? ')
	print(f'Hello, {user_name}!')
	print(game_name.DESCRIPTION)

	for round_number in range(MAX_ROUND):
		question, correct_answer = game_name.make_question_and_correct_answer()
		print(f"Question: {question}")
		user_answer = prompt.string("Your answer: ")

		if not (user_answer == correct_answer):
			print(f" '{user_answer}' is wrong answer ;(. "
			      f"Correct answer was '{correct_answer}'."
			      f"Let's try again, {user_name}!")
			return
		print("Correct!")

	print(f'Congratulations, {user_name}!')