def sieve_of_eratosthenes() -> tuple:
    n = 0
    while True:
        try:
            n = int(input(f"Введите до какого числа выбирать простые числа: "))
            break
        except ValueError:
            print(f"Неверный ввод. Повторите попытку.")
            continue

    primes = list()
    sieve = set(range(2, n + 1))
    while sieve:
        prime = min(sieve)
        primes.append(prime)
        sieve -= set(range(prime, n + 1, prime))

    print(f"Массив простых чисел: \n{primes}\n")
    return primes, n


def first_exercise():
    print("Задание 1:")
    while True:
        tup = sieve_of_eratosthenes()
        primes = tup[0]
        n = tup[1]
        try:
            number = int(input(f"Введите номер числа, которое нужно вывести (от 1 до {len(primes)}): "))
            if 0 < number <= n:
                print(f"Число с номером {number}: {find_prime(primes, number - 1)}\n")
                break
            else:
                print("Неверный ввод. Повторите попытку.")
                continue
        except Exception:
            print(f"Неверный ввод. Повторите попытку.")
            continue


def find_prime(primes: list, number: int) -> int:
    return primes[number]

