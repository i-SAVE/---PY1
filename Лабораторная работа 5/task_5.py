import random
import string


def get_random_password(password_size, alpha=string.ascii_letters + string.digits) -> str:
    lst_ = random.sample(alpha, password_size)
    return "".join(lst_)


print(get_random_password(8))

...  # TODO написать функцию генерации случайных паролей
