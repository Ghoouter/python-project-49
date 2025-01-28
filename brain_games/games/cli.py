import prompt


def welcome_user():
		username = prompt.string('May I have your name? ')
		return f'Hello, {username}'