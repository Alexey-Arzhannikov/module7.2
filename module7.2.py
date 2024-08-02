from pprint import pprint


def custom_write(file_name, strings):
    list_tell = []  # Список номеров байтов, на которых началась запись строки
    list_number_str = []  # Номера записанных строк
    number = 0
    with open(file_name, "a", encoding='utf-8') as file:  # Оикрываем файл в режиме добавления
        for i in strings:
            list_tell.append(file.tell())  # Добавляем номера байтов в список list_tell
            number += 1
            list_number_str.append(number)  # Добавляем номера строк в список list_number_str
            file.write(f'{i}\n')  # Добавляем строку в файл с переносом на следующую строку
    tuple_key = list(zip(list_number_str, list_tell)) # Упаковываем два списка в один
    ''' Создаем словарь из списка tuple_key(его елементы - ключи(tuple))
    и переданного списка strings(елементы - значения(str)) в аргумент функии'''
    dict_res = dict(zip(tuple_key, strings))
    pprint(dict_res)


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]


custom_write('test7.2.txt', info)
