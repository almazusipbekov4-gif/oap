print("=== ЗАДАНИЕ 1. Функции и параметры ===")
def add(a, b):
    return a + b

def power(a, n=2):
    return a ** n

def sum_all(*args):
    total = 0
    for value in args:
        total += value
    return total

print("add(5, 3) =", add(5, 3))
print("power(4) =", power(4))  # с параметром по умолчанию (квадрат)
print("power(2, 3) =", power(2, 3))
print("sum_all(1, 2, 3, 4, 5) =", sum_all(1, 2, 3, 4, 5))


print("\n=== ЗАДАНИЕ 2. Область видимости переменных ===")
global_var = 100  # Глобальная переменная

def modify_global():
    global global_var  # Ключевое слово для изменения глобальной переменной внутри функции
    global_var = 200
    local_var = 50     # Локальная переменная
    print(f"Внутри функции: global_var = {global_var}, local_var = {local_var}")

print(f"До вызова функции global_var = {global_var}")
modify_global()
print(f"После вызова функции global_var = {global_var}")
print("Разница: Локальные переменные существуют только внутри функции, а глобальные видны во всем модуле.")


print("\n=== ЗАДАНИЕ 3. Рекурсивный и итерационный факториал ===")
# Рекурсивная версия
def factorial_recursive(n):
    if n == 0 or n == 1: # Базовый случай
        return 1
    return n * factorial_recursive(n - 1) # Рекурсивный вызов

# Итерационная версия
def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

n_val = 5
print(f"Факториал {n_val} (рекурсивно):", factorial_recursive(n_val))
print(f"Факториал {n_val} (итерационно):", factorial_iterative(n_val))


print("\n=== ЗАДАНИЕ 4 & Задача 6. Рекурсивная сумма цифр числа ===")
def sum_digits(n):
    n = abs(n)  # Обработка отрицательных чисел
    if n < 10:  # Базовый случай
        return n
    return (n % 10) + sum_digits(n // 10) # Рекурсивный шаг

print("Сумма цифр числа 1234:", sum_digits(1234))
print("Сумма цифр числа 245:", sum_digits(245))


print("\n=== ЗАДАНИЕ 5 & Задача 8. Рекурсивный поиск максимального элемента ===")
def max_element(arr, index=0):
    # Базовый случай: если дошли до последнего элемента
    if index == len(arr) - 1:
        return arr[index]
    
    # Рекурсивный вызов для оставшейся части списка
    sub_max = max_element(arr, index + 1)
    
    # Возвращаем наибольшее из текущего и найденного далее
    return arr[index] if arr[index] > sub_max else sub_max

my_list = [3, 15, 7, 99, 42, 8]
print(f"Максимальный элемент в списке {my_list}:", max_element(my_list))


print("\n=== Дополнительно: Числа Фибоначчи и оптимизация ===")
# Обычная рекурсия (медленная для больших n из-за повторных вычислений)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print("Число Фибоначчи (n=6):", fibonacci(6))


print("\n=== ПРАКТИЧЕСКИЕ ЗАДАЧИ ===")
# Задача 1
def average(a, b, c):
    return (a + b + c) / 3
print("Задача 1 (Среднее арифм. 3, 6, 9):", average(3, 6, 9))

# Задача 2
def is_even(n):
    return n % 2 == 0
print("Задача 2 (Четное ли 4?):", is_even(4))

# Задача 5
def print_from_n_to_1(n):
    if n < 1:
        return
    print(n, end=" ")
    print_from_n_to_1(n - 1)
print("Задача 5 (От 5 до 1):", end=" ")
print_from_n_to_1(5)
print()

# Задача 7 (Рекурсивная проверка палиндрома)
def is_palindrome(text):
    text = text.lower().replace(" ", "")
    if len(text) <= 1:
        return True
    if text[0] != text[-1]:
        return False
    return is_palindrome(text[1:-1])

print("Задача 7 ('radar' — палиндром?):", is_palindrome("radar"))
print("Задача 7 ('python' — палиндром?):", is_palindrome("python"))

# Задача 9 (Быстрое возведение в степень рекурсивно)
def fast_pow(a, n):
    if n == 0:
        return 1
    if n < 0:
        return 1 / fast_pow(a, -n)
    if n % 2 == 0:
        half = fast_pow(a, n // 2)
        return half * half
    else:
        return a * fast_pow(a, n - 1)

print("Задача 9 (Быстрая степень 2^10):", fast_pow(2, 10))

# Задача 10 (Подсчёт глубины рекурсии)
def count_depth(n):
    if n <= 0:
        return 0
    return 1 + count_depth(n - 1)

print("Задача 10 (Глубина рекурсии для n=5):", count_depth(5))