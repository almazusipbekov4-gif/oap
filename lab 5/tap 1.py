print("=== ЗАДАНИЕ 1. Создание и ввод массива ===")
# Считывание количества элементов с проверкой, что n > 0
while True:
    try:
        n = int(input("Введите количество элементов массива (n > 0): "))
        if n > 0:
            break
        print("Ошибка: количество элементов должно быть больше 0.")
    except ValueError:
        print("Ошибка: введите целое число.")

# Ввод элементов массива с помощью цикла for
arr = []
for i in range(n):
    while True:
        try:
            elem = int(input(f"Введите элемент {i + 1}: "))
            arr.append(elem)
            break
        except ValueError:
            print("Ошибка: введите целое число.")

print("Полученный массив:", arr)


print("\n=== ЗАДАНИЕ 2. Обработка массива (без использования sum, max, min) ===")
if len(arr) > 0:
    # Инициализация начальных значений
    total_sum = 0
    max_elem = arr[0]
    min_elem = arr[0]

    # Самостоятельная реализация алгоритмов перебора и обработки
    for item in arr:
        total_sum += item
        if item > max_elem:
            max_elem = item
        if item < min_elem:
            min_elem = item

    average = total_sum / len(arr)

    print(f"Сумма элементов: {total_sum}")
    print(f"Максимальный элемент: {max_elem}")
    print(f"Минимальный элемент: {min_elem}")
    print(f"Среднее арифметическое: {average}")


print("\n=== ЗАДАНИЕ 3. Подсчёт по условию ===")
positive_count = 0
negative_count = 0
even_count = 0

for item in arr:
    if item > 0:
        positive_count += 1
    elif item < 0:
        negative_count += 1
    
    if item % 2 == 0:
        even_count += 1

print(f"Количество положительных чисел: {positive_count}")
print(f"Количество отрицательных чисел: {negative_count}")
print(f"Количество чётных элементов: {even_count}")


print("\n=== ЗАДАНИЕ 4. Линейный поиск ===")
try:
    search_value = int(input("Введите число для поиска в массиве: "))
    found_index = -1

    # Ручной линейный поиск с использованием break
    for i in range(len(arr)):
        if arr[i] == search_value:
            found_index = i
            break

    if found_index != -1:
        print(f"Число {search_value} найдено под индексом: {found_index}")
    else:
        print(f"Число {search_value} отсутствует в массиве.")
except ValueError:
    print("Ошибка: введено не целое число для поиска.")


print("\n=== ЗАДАНИЕ 5 (Повышенной сложности). Второй по величине элемент ===")
if len(arr) < 2:
    print("Длина массива меньше 2, невозможно определить второй по величине элемент.")
else:
    # Создаем копию или ищем логически без изменения исходного массива
    # Убираем дубликаты максимального элемента корректно
    unique_sorted = sorted(list(set(arr)), reverse=True)
    
    if len(unique_sorted) < 2:
        print("В массиве все элементы одинаковые, второго по величине уникального элемента нет.")
        # Альтернативный подход строго по индексам/значениям с дубликатами, если требуется:
        # Находим первое и второе максимальное значение простым обходом:
    
    # Классический алгоритм поиска второго по величине элемента обходом:
    first_max = float('-inf')
    second_max = float('-inf')

    for item in arr:
        if item > first_max:
            second_max = first_max
            first_max = item
        elif item > second_max and item != first_max:
            second_max = item

    if second_max == float('-inf'):
        print("Второй по величине элемент отсутствует (все элементы равны).")
    else:
        print(f"Второй по величине элемент: {second_max}")