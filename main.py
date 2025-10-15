from user_manager import UserManager
from user import User
from user_not_found_error import UserNotFoundError
from user_already_exists_error import UserAlreadyExistsError

from datetime import datetime
import logging

logging.basicConfig(
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

SPLIT_LINE = "\n" + "#" * 100 + "\n"

NON_UNIQUE_USERNAME = "yuri.abele"
NOT_EXISTING_USERNAME = "not.exists"

user_manager = UserManager()

print(SPLIT_LINE)

# Add unique users
print("==> Adding unique users...")

user1 = User(username=NON_UNIQUE_USERNAME, email="yuri.abele@domain.my", age=54)
user_manager.add_user(user1)
print(f"User \"{user1.username}\" added successfully.")

user2 = User(username="my.darling", email="darling@family.my", age=17) # вечные 17 ;-)
user_manager.add_user(user2)
print(f"User \"{user2.username}\" added successfully.")

print(SPLIT_LINE)

# Try to add non-unique user
try:
	print(f"==> Trying to add user with existing username \"{NON_UNIQUE_USERNAME}\"...")
	user3 = User(username=NON_UNIQUE_USERNAME, email="other.yuri@other.domain", age=33)
	user_manager.add_user(user3)

	print(f"\tUser \"{NON_UNIQUE_USERNAME}\" added successfully.")
except UserAlreadyExistsError as e:
	logging.exception(e)
	print(f"ERROR: User \"{NON_UNIQUE_USERNAME}\" already exists, so cannot be added again.")

print(SPLIT_LINE)

# Try to delete not existing user
try:
	user_not_exists = user_manager.find_user(NOT_EXISTING_USERNAME)
except UserNotFoundError as e:
	logging.exception(e)
	print(f"ERROR: User '{NOT_EXISTING_USERNAME}' does not exist, so cannot be deleted.")

print(SPLIT_LINE)

#####################################################

print(f"\n{"="*50}\nFinished at: {datetime.now():%Y-%m-%d %H:%M:%S}\n\n")