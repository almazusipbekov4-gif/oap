grades = [70, 80, 90]
print(sum(grades) / (len(grades) - 1))

def calculate_average(grades: list[float]) -> float | None:
    if not grades:
        return None
    return sum(grades) / len(grades)


def main():
    test_cases = [
        [70, 80, 90],
        [100],
        [],
        [0, 0, 0],  # дополнительный граничный тест: нулевые оценки
    ]

    for case in test_cases:
        avg = calculate_average(case)
        if avg is None:
            print(f"Вход {case}: список оценок пуст, вычислить среднее невозможно.")
        else:
            print(f"Вход {case} -> Средний балл: {avg:.1f}")


if __name__ == "__main__":
    main()