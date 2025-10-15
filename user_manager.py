from .user_not_found_error import UserNotFoundError
from .user_already_exists_error import UserAlreadyExistsError
from .user import User

# Dictionary to store users with username as key and User object as value
users: dict[str, User] = {}

class UserManager:
	def __init__(self):
		self.users = {}

	def add_user(self, user: User):
		if user.username in self.users.keys:
			raise UserAlreadyExistsError(f"User \"{username}\" already exists")
		self.users[user.username] = user

	def remove_user(self, username: str):
		if username not in self.users:
			raise UserNotFoundError(f"User \"{username}\" does not exist")
		del self.users[username]

	def find_user(self, username: str):
		found_user = self.users.get(username, None)
		if found_user is None:
			raise UserNotFoundError(f"User \"{username}\" does not exist")
		return found_user
