from data_create import *
from data_edit import *


def start() -> None:
    action = input('Выберите действие: 1 - запись, 2 - чтение, 3- редактирование, 4 - удаление\n')
    if action == '1':  # запись данных
        write_number()
    elif action == '2':  # чтение данных
        read_number()
    elif action == '3':  # редактирование данных
        edit_number()
    elif action == '4':  # удаление данных
        del_number()


def write_number() -> None:  # функция записи в файл
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()

    var = int(input(f"В каком формате записать данные?\n"
                    f"Вариант 1: \n{name}\n{surname}\n{phone}\n{address}\n\n"
                    f"Вариант 2: {name};{surname};{phone};{address}\n"
                    f"Выберите вариант: "))

    while var != 1 and var != 2:
        print('Неправильный ввод.')
        var = int(input('Введите число: '))

    if var == 1:
        with open('data_first_variant.csv', 'a', encoding='utf-8') as file:
            file.write(f'{name}\n{surname}\n{phone}\n{address}\n\n')
    elif var == 2:
        with open('data_second_variant.csv', 'a', encoding='utf-8') as file:
            file.write(f'{name};{surname};{phone};{address}\n\n')


def read_number() -> None:  # функция чтения и вывода данных
    print(f'Выводим первый файл: ')
    print(*search_user_file1())
    print('Выводим второй файл: ')
    print(*search_user_file2())


def edit_number() -> None:  # редактирование данных
    res = check_user()  # проверяем наличие записи
    if res:  # если такая запись есть - начинаем редактирование
        print(f'Найдена запись: {res[0]}')
        print('Введите новые данные для этой записи.')

        ## Ввод новых данных
        name = name_data()
        surname = surname_data()
        phone = phone_data()
        address = address_data()
        file_number = res[1]  # Номер файла в котором нужно изменить данные
        last_data = res[0]  # Запись, которую меняем

        edit_user(name, surname, phone, address, file_number, last_data)  # функция редактирования

    else:  # если записи нет - завершаем функцию
        print('Информация не найдена')


def del_number() -> None:
    res = check_user()  # проверяем наличие записи
    if res:  # если такая запись есть - вызываем функцию удаления
        del_user(res[0], res[1])
    else:  # если записи нет - завершаем функцию
        print('Информация не найдена')
