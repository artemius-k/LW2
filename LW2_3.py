

def third_exercise():
    print("Задание 3:")
    while True:
        print("Меню: \n"
              "1. Ввести матрицу. \n"
              "0. Выход. \n")

        choice = int()
        try:
            choice = int(input())
            if choice != 0 and choice != 1:
                print("Неверный ввод данных. Повторите попытку")
                continue
        except (TypeError, ValueError):
            print("Неверный ввод данных. Повторите попытку")
            continue
        finally:
            if choice == 0:
                break

        array_size = int()
        while True:
            try:
                array_size = int(input("Введите порядок матрицы: "))
                break
            except (TypeError, ValueError):
                print("Неверный ввод данных. Повторите попытку: ", end=" ")
                continue

        array = [[0]*array_size for i in range(array_size)]

        print("Введите матрицу: ")
        while True:
            try:
                for i in range(array_size):
                    for j in range(array_size):
                        array[i][j] = int(input(f"Элемент array[{i}][{j}]: "))
                break
            except (TypeError, ValueError):
                print("Неверный ввод данных. Повторите попытку: ", end=" ")
                continue
        print(f"Начальный массив:\n{array}")

        negative_sum = 0
        counter = 0
        for j in range(array_size):
            for i in range(array_size):
                if array[i][j] < 0:
                    counter = counter+1
            if counter == array_size:
                print(f"Номер столбца с отрицательными элементами: {j}")
                for k in range(array_size):
                    negative_sum = negative_sum + array[k][j]
                    array[k].pop(j)
                break
            else:
                counter = 0
        print(f"Сумма отрицательных элементов: {negative_sum}")
        print(f"Конечный массив: \n{array}")