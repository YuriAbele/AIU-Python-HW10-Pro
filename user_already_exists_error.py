class UserAlreadyExistsError(Exception):
	"""Исключение, возникающее при попытке создать пользователя с уже существующим именем или email."""
	pass