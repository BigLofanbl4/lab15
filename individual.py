#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def func_decorator(func):
    def wrapper(*args, **kwargs):
        return_value = func(*args, **kwargs)
        while "--" in return_value:
            return_value = return_value.replace("--", "-")
        return return_value
    return wrapper


@func_decorator
def to_lat(string):
    t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
        'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
        'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
        'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya',
        '!': '-', '?': '-', ':': '-', ';': '-', '.': '-', ',': '-', '_': '-'}
        
    string = string.lower()
    for key, val in t.items():
        string = string.replace(key, val)
    return string


if __name__ == "__main__":
    print(to_lat("Привет!!!---Мир??.."))