import random
import string

alpha = string.ascii_letters + string.digits


def get_random_password(password_size) -> str:
    lst_ = random.sample(alpha, password_size)
    return " ".join(map(str, lst_))


print(get_random_password(8))

...  # TODO написать функцию генерации случайных паролей
