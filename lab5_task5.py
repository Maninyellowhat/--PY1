
from random import choice
from string import ascii_letters, digits

def get_random_password() -> str:
    password_rand = ascii_letters + digits
    i = 8
    password = ''.join(choice(password_rand) for _ in range(i))
    return password


print(get_random_password())
