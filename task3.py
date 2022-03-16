
import os
from datetime import datetime

nested_list = [['a', 'b', 'c'],['d', 'e', 'f', 'h', False],[1, 2, None],]

FILE_PATH = 'decorator_3.txt'


def logg_path(path):
    p = os.path.abspath('decorator_3.txt')
    def decor_logger (old_function):
        def new_function (*args, **kwargs):
            date_time = datetime.now()
            func_name = old_function.__name__
            result = list(old_function(*args, **kwargs))
            object_type = old_function(*args, **kwargs)
            with open('decorator_3.txt', 'a', encoding='utf-8') as file:
                file.write(f'Путь: {p}\n'
                           f'Дата/время: {date_time}\n'
                           f'Имя функции: {func_name}\n'
                           f'Аргументы: {args, kwargs}\n'
                           f'Результат: {result}\n'
                           f'Тип объекта: {object_type}\n')
            return result
        return new_function
    return decor_logger


@logg_path(FILE_PATH)
def flat_generator(list_of_lists):
    for x in list_of_lists:
        for j in x:
            yield j

if __name__ == '__main__':
    for item in flat_generator(nested_list):
        if type(item) == bool:
            print(item)
        elif type(item) == int:
            print(item)
        elif item is None:
            print(item)
        else:
            print(f"'{item}'")
    print()
    flat_list = [item for item in flat_generator(nested_list)]
    print(flat_list)