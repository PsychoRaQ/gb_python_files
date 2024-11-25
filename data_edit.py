def check_user() -> tuple | None:
    try:
        name, surname = input('Введите имя и фамилию в формате * Иван Иванов *\n').split()
    except:
        return None
    file_number = int(input('Введите номер файла, в котором хотите изменить информацию: \n'
                            '1 - первый файл\n'
                            '2 - второй файл\n'))
    while file_number not in (1, 2):
        print('Не верный номер.')
        file_number = int(input('Введите номер файла: '))

    if file_number == 1:
        res = search_user_file1()
    elif file_number == 2:
        res = search_user_file2()

    for i in res:
        if name in i and surname in i:
            return i, file_number
    return None


def search_user_file1() -> list:  # Поиск записи в первом файле
    with open('data_first_variant.csv', 'r', encoding='utf-8') as file:
        data_first = file.readlines()
        data_first_lst = []
        j = 0
        for i in range(len(data_first)):
            if data_first[i] == '\n' or i == len(data_first_lst) - 1:
                data_first_lst.append(''.join(data_first[j:i + 1]))
                j = i
    return data_first_lst


def search_user_file2() -> list:  # Поиск записи во втором файле
    with open('data_second_variant.csv', 'r', encoding='utf-8') as file:
        data_second = file.readlines()
    return data_second


def give_file(file_number) -> tuple:  # Получение данных о файле по его номеру
    if file_number == 1:
        file_name = 'data_first_variant.csv'
        data = search_user_file1()
    elif file_number == 2:
        file_name = 'data_second_variant.csv'
        data = search_user_file2()
    return file_name, data


def edit_user(name, surname, phone, address, file_number, last_data) -> None:  # Редактирование записи
    file_name, data = give_file(file_number)

    for index, value in enumerate(data):  # Ищем в списке нужную запись, и меняем ее в формате (зависит от номера файла)
        if value == last_data:
            if file_number == 1:
                data[index] = f'{name}\n{surname}\n{phone}\n{address}\n\n'
                break
            elif file_number == 2:
                data[index] = f'{name};{surname};{phone};{address}'
                break
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(''.join(data))
    print('Данные успешно изменены!')


def del_user(last_data, file_number) -> None:
    file_name, data = give_file(file_number)
    for index, value in enumerate(data):  # Ищем в списке нужную запись и удаляем её.
        if value == last_data:
            del data[index]
            break
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(''.join(data))
    print('Данные успешно удалены!')
