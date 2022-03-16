import os
from datetime import datetime

nested_list = [['a', ['b', ['c']], [['d', ['e']], 'f'], [1, 2, None], ]]

FILE_PATH = 'decorator_2.txt'


def logg_path(path):
    p = os.path.abspath('decorator_2.txt')

    def decor_logger(old_function):
        def new_function(*args, **kwargs):
            date_time = datetime.now()
            func_name = old_function.__name__
            result = old_function(*args, **kwargs)
            with open('decorator_2.txt', 'a', encoding='utf-8') as file:
                file.write(f'Путь: {p}\n'
                           f'Дата/время: {date_time}\n'
                           f'Имя функции: {func_name}\n'
                           f'Аргументы: {args, kwargs}\n'
                           f'Результат: {result}\n')
            return result

        return new_function

    return decor_logger


@logg_path(FILE_PATH)
def flatten(s):
    if s == []:
        return s
    if isinstance(s[0], list):
        return (flatten(s[0]) + flatten(s[1:]))
    return (s[:1] + flatten(s[1:]))


print(flatten(nested_list))

if __name__ == '__main__':
    flatten(nested_list)
