import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(INPUT_FILE) -> list[dict]:
    list_ = []
    with open(INPUT_FILE) as thing:
        header_value = thing.readline().strip('\n').split(",")
        for row in thing:
            value = row.strip("\n").split(",")  # мы strip("\n") --> replace("\n", "")
            list_.append(dict(zip(header_value, value)))
    return list_


...  # TODO реализовать конвертер из csv в json

print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
