import random

print("=== ЗАДАНИЕ 1 (Базовый уровень) ===")
# Запрос размеров матрицы
rows = int(input("Введите количество строк: "))
cols = int(input("Введите количество столбцов: "))

# Формирование двумерного массива из случайных чисел от 1 до 20
matrix = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(random.randint(1, 20))
    matrix.append(row)

print("\nМатрица:")
for row in matrix:
    for value in row:
        print(f"{value:4}", end="")
    print()

# Поиск суммы всех элементов и максимального элемента
total = 0
maximum = matrix[0][0]
for row in matrix:
    for value in row:
        total += value
        if value > maximum:
            maximum = value

print("\nСумма элементов:", total)
print("Максимальный элемент:", maximum)


print("\n=== ЗАДАНИЕ 2 (Средний уровень) ===")
# Сумма по строкам
row_sums = []
for i in range(rows):
    row_sum = sum(matrix[i])
    row_sums.append(row_sum)
    print(f"Сумма строки {i}: {row_sum}")

# Сумма по столбцам
for j in range(cols):
    col_sum = 0
    for i in range(rows):
        col_sum += matrix[i][j]
    print(f"Сумма столбца {j}: {col_sum}")

# Поиск строки с максимальной суммой
max_row_index = row_sums.index(max(row_sums))
print("Строка с максимальной суммой (индекс):", max_row_index)


print("\n=== ЗАДАНИЕ 3 (Повышенный уровень) ===")
# Упрощенная версия игрового поля 4х4 с сдвигом вправо
game_matrix = [
    [0, 2, 0, 4],
    [1, 0, 3, 0],
    [0, 0, 5, 6],
    [7, 0, 0, 8]
]

print("До сдвига:")
for row in game_matrix:
    print(row)

def shift_right(row):
    new_row = [x for x in row if x != 0]
    zeros = [0] * (len(row) - len(new_row))
    return zeros + new_row

for i in range(4):
    game_matrix[i] = shift_right(game_matrix[i])

print("\nПосле сдвига вправо:")
for row in game_matrix:
    print(row)