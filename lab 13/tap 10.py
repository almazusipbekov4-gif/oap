with open("scores.txt", "r", encoding="utf-8") as f:
    print(f.read())

    from pathlib import Path


def read_scores_file(filepath: str = "scores.txt") -> str:
    path = Path(filepath)
    with path.open("r", encoding="utf-8") as f:
        return f.read()


def main():
    target = "scores.txt"
    print(f"Ожидаемый путь к файлу: {Path(target).resolve()}")

    try:
        content = read_scores_file(target)
    except FileNotFoundError:
        print(f"Ошибка: файл '{target}' не найден. Поместите его рядом с main.py.")
    else:
        if content == "":
            print("Файл пуст (пустой вывод).")
        else:
            print("Содержимое файла:")
            print(content)

    # Дополнительный граничный тест: заведомо несуществующий файл
    try:
        read_scores_file("missing_test_file.txt")
    except FileNotFoundError:
        print("Граничный тест пройден: корректно обработан отсутствующий файл 'missing_test_file.txt'.")


if __name__ == "__main__":
    main()