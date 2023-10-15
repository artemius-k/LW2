def second_exercise():
    while True:
        print(f"Задание 2: \n"
              f"1 - Ввести список. \n"
              f"2 - Ввести словарь. \n"
              f"3 - Ввести число. \n"
              f"4 - Ввести строку. \n"
              f"0 - Выход из задания.")

        try:
            choice = int(input())
            if 0 > choice > 4:
                print(f"Пункт в меню не найден. Повторите попытку. ")
                continue
        except Exception:
            print(f"Неверный ввод, повторите попытку.")
            continue

        if choice == 0:
            break
        elif choice == 1:
            user_input = enter_list()
        elif choice == 2:
            user_input = enter_dict()
        elif choice == 3:
            user_input = enter_value()
        elif choice == 4:
            user_input = input("Введите строку: ")

        work_with_collections(user_input)


def enter_list() -> list:
    my_list = list()

    while True:
        try:
            element = input(f"Введите число для списка (для выхода введите 'BREAK'): ")
            if element == "BREAK":
                break
            else:
                my_list.append(float(element))
                continue
        except Exception:
            print(f"Неверный ввод, повторите попытку.")
            continue

    return my_list


def enter_dict() -> dict:
    my_dict = dict()
    print(f"Введите словарь. \n"
          f"(для прекращения ввода при запросе 'Введите ключ' введите 'BREAK'): \n")

    while True:
        key = input(f"Введите ключ: ")
        if key == 'BREAK':
            break
        val = input(f"Введите значение: ")
        my_dict.update({key: val})

    return my_dict


def enter_value() -> int:
    while True:
        try:
            my_val = int(input("Введите целое положительное число: "))
            if my_val <= 0:
                print(f"Число неположительное. Повторите ввод.")
                continue
            break
        except Exception:
            print(f"Неверный ввод, повторите попытку.")
            continue

    return my_val


def work_with_collections(user_input: any):
    counter = 0
    j = 0

    if isinstance(user_input, list):
        print("Начальный список: ", *user_input)
        max_value = user_input[0]

        for i in user_input:
            if (i % 2 == 0):
                counter = counter + 1
            if (i >= max_value):
                max_value = i

        while j < len(user_input):
            if user_input[j] < 0:
                del user_input[j]
            j = j + 1

        print(f"Количество чётных чисел: {counter}\n"
              f"Максимальное число в списке: {max_value}\n"
              "Список без отрицательных: ", *user_input)

    elif isinstance(user_input, dict):
        print("Неотсортированный словарь", user_input)
        sorted_dict = dict(sorted(user_input.items(), key=lambda item: item[1]))
        print("Отсортированный словарь: ", sorted_dict)

    elif isinstance(user_input, int):
        reversed_value = str(user_input)[::-1]
        print("Инверсированное число: ", reversed_value)

    elif isinstance(user_input, str):
        values_dict = dict()
        for i in user_input:
            for j in user_input:
                if i == j: counter = counter + 1
            values_dict.update({i: counter})
            counter = 0
        print("Количество вхождений каждого символа: ", values_dict)
