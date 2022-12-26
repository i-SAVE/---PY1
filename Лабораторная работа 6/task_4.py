import json

INPUT_FILE = "input.csv"


def csv_to_list_dict_test(INPUT_FILE) -> list[dict]:
    with open(INPUT_FILE) as thing:
        header_value = thing.readline()[:-1].split(",")
        list_ = [(dict(zip(header_value, row[:-1].split(",")))) for row in thing]
# мы исп. срез [:-1],ведь известно что последний элемент строки это перенос строки.
    return list_


...  # TODO реализовать конвертер из csv в json

print(json.dumps(csv_to_list_dict_test(INPUT_FILE), indent=4))
