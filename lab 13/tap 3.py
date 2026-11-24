a = input("Сумма: ")
b = input("Количество: ")
print(a / b)

def average_reading(a_raw: str, b_raw: str) -> float:
    a = float(a_raw)
    b = float(b_raw)
    if b == 0:
        raise ZeroDivisionError("Количество не может быть равно нулю.")
    return a / b


def main():
    cases = [
        ("20", "4"),
        ("0", "2"),
        ("5", "0"),
        ("12.5", "abc"),  # дополнительный граничный/ошибочный тест: нечисловой ввод
    ]

    for a_in, b_in in cases:
        try:
            avg = average_reading(a_in, b_in)
        except ValueError:
            print(f"Вход ({a_in!r}, {b_in!r}) -> Ошибка: введите корректные числа.")
        except ZeroDivisionError as e:
            print(f"Вход ({a_in!r}, {b_in!r}) -> Ошибка: {e}")
        else:
            print(f"Вход ({a_in!r}, {b_in!r}) -> Среднее: {avg}")


if __name__ == "__main__":
    main()