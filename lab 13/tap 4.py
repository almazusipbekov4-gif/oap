values = [3, 8, 5]
maximum = 0
for v in values:
    if v < maximum:
        maximum = v
print(maximum)

def find_max(values: list[float]) -> float | None:
    if not values:
        return None
    maximum = values[0]
    for v in values[1:]:
        if v > maximum:
            maximum = v
    return maximum


def main():
    cases = [
        [3, 8, 5],
        [-4, -2],
        [],
        [-10],  # дополнительный граничный тест: один отрицательный элемент -> -10
    ]

    for case in cases:
        res = find_max(case)
        if res is None:
            print(f"Вход {case} -> Список пуст, максимум не определён.")
        else:
            print(f"Вход {case} -> Максимум: {res}")


if __name__ == "__main__":
    main()