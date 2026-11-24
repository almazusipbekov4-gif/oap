def count_positive(values: list[float]) -> int:
    count = 0
    for v in values:
        if v > 0:
            count += 1
    return count


def main():
    cases = [
        [-2, 0, 4, 7],
        [0],
        [],
        [-5, -1, 0],  # дополнительный граничный тест: нет положительных -> 0
    ]

    for case in cases:
        print(f"Вход {case} -> Положительных: {count_positive(case)}")


if __name__ == "__main__":
    main()