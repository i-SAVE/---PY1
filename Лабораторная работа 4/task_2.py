def get_count_char(str_):
    dictionary_ = dict()  # создадим словарь пустой

    # str_ = ''.join(str_.split()) - нет необходимости

    str_ = str_.lower()  # приводим строку к нижнему регистру
    for key in str_:  # использую цикл для словаря
        if key.isalpha():
            count = str_.count(key)
            dictionary_[key] = count
    return dictionary_


# данный код намного короче и удобнее для понимания - чем с get() и 2 усл.

...  # TODO посчитать количество каждой буквы в строке в аргументе str_

main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

print(get_count_char(main_str))
