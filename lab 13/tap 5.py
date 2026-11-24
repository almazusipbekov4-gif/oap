def check_access(age_raw: str) -> str:
    age = int(age_raw)
    if age < 0 or age > 130:
        raise ValueError("Некорректный возраст.")
    if age >= 18:
        return "Доступ"
    return "Нет доступа"


def main():
    cases = [
        "18",
        "17",
        "-2",
        "0",  # дополнительный граничный тест: возраст 0 -> Нет доступа
    ]

    for raw in cases:
        try:
            print(f"Возраст={raw!r} -> {check_access(raw)}")
        except ValueError as e:
            print(f"Возраст={raw!r} -> Ошибка: {e}")


if __name__ == "__main__":
    main()