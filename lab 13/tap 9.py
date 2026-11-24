scores = {"A": 90, "B": 75}
name = input("Код: ")
print(scores[name])

def get_score(scores: dict[str, int], code: str) -> int | None:
    return scores.get(code.strip())


def main():
    scores = {"A": 90, "B": 75}
    cases = [
        "A",
        "B",
        "C",
        " a ",  # дополнительный граничный тест: пробелы и нижний регистр -> None / сообщение
    ]

    for code in cases:
        val = get_score(scores, code)
        if val is None:
            print(f"Код {code!r} -> Оценка не найдена (ключ отсутствует).")
        else:
            print(f"Код {code!r} -> Оценка: {val}")


if __name__ == "__main__":
    main()