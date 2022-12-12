# TODO решить с помощью list comprehension и распечатать его
import pprint  # максимальное число в списке

numbers = [{"bin": bin(n), "dec": n, "hex": hex(n), "oct": oct(n)} for n in
           range(0, 16)]  # для цикла от 0 - 15
# находим словари с помощью list comprehension

pprint.pprint(numbers)  # печатаем его
