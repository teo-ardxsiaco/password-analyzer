import getpass as gp
import os
import sys

password = gp.getpass("Enter your password: ")
print("Password entered.\n")

enough_length = True
symbol_check = False
uppercase_check = False
lowercase_check = False
number_check = False

if len(password) < 8:
    enough_length = False


if not password.isalnum():
    symbol_check = True

for char in password:
    if char.isupper():
        uppercase_check = True
    if char.islower():
        lowercase_check = True
    if char.isdigit():
        number_check = True

if (
    not symbol_check
    or not uppercase_check
    or not lowercase_check
    or not number_check
    or not enough_length
):
    print(
        "Password must be 8 characters long, contain at least one symbol, one uppercase letter, one lowercase letter, and one number."
    )
    print("Restarting script...\n")
else:
    print("Password meets all requirements.\n")

os.execv(sys.executable, [sys.executable] + sys.argv)