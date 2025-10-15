class User:
	"""
	Базовый класс, представляющий пользователя.
	"""

	def __init__(self, username: str, email: str, age: int):

		# Нормализуем входные данные на случай, если кто-то будет создавать пользователя напрямую
		# (вместо использования метода UsersService.register)
		normalized_username = username.strip().lower() # Usernames не чувствительны к регистру
		normalized_email = email.strip() # Email может быть с заглавными буквами

		self.username = normalized_username
		self.email = normalized_email
		self.age = age

	def __str__(self):
		return self.__repr__()

	def __repr__(self):
		return f"User(username=\"{self.username}\", email=\"{self.email}\", password=\"<CENSORED>\")"
