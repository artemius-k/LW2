import LW2_1
import LW2_2
import LW2_3


def main():  # Lab №2 - Variant 15
    while True:
        print("Главное меню: \n"
              "Задание 1 - Простые числа; \n"
              "Задание 2 - Функция для работы с коллекциями; \n"
              "Задание 3 - Матрица; \n"
              "0 - Выход. \n")

        try:
            choice = int(input(f"Ввод: "))
        except ValueError:
            print(f"Неверный ввод. Повторите попытку.")
            continue

        print(f"")
        if choice == 0:
            break
        elif choice == 1:
            LW2_1.first_exercise()
        elif choice == 2:
            LW2_2.second_exercise()
        elif choice == 3:
            LW2_3.third_exercise()
        else:
            print(f"Неверный ввод.")
            continue
    return


main()
