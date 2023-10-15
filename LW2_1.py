print("Задание 1:")

# Sieve of Eratosthenes
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


def first_exercise():
    while True:
        try:
            number = int(input(f"Введите номер числа, которое нужно вывести (от 1 до {len(primes)}): "))
            if 0 < number <= n:
                break
            else:
                print("Неверный ввод. Повторите попытку.")
                continue
        except Exception:
            print(f"Неверный ввод. Повторите попытку.")
            continue
    print(f"Число с номером {number}: {find_prime(number - 1)}\n")


def find_prime(number: int) -> int:
    return primes[number]


first_exercise()
