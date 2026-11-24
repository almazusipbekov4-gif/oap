def check_temperature(temp_raw: str) -> str:
    temperature = float(temp_raw)
    if temperature >= 37.5:
        return "Повышена"
    return "Норма"


def main():
    cases = [
        "37.5",
        "36.6",
        "abc",
        "37.4",  # дополнительный граничный тест: чуть ниже порога -> Норма
    ]

    for raw in cases:
        try:
            print(f"Температура={raw!r} -> {check_temperature(raw)}")
        except ValueError:
            print(f"Температура={raw!r} -> Ошибка: введите числовое значение.")


if __name__ == "__main__":
    main()