items = [10, 20, 30]
index = int(input("Индекс: "))
print(items[index])

def get_item_by_index(items: list, index_raw: str):
    index = int(index_raw)
    if index < 0 or index >= len(items):
        raise IndexError(f"Индекс {index} вне диапазона 0..{len(items) - 1}.")
    return items[index]


def main():
    items = [10, 20, 30]
    cases = [
        "1",
        "2",
        "3",
        "0",  # дополнительный граничный тест: первый элемент по индексу 0 -> 10
    ]

    for idx_raw in cases:
        try:
            val = get_item_by_index(items, idx_raw)
            print(f"Индекс={idx_raw} -> Элемент: {val}")
        except ValueError:
            print(f"Индекс={idx_raw!r} -> Ошибка: введите целое число.")
        except IndexError as e:
            print(f"Индекс={idx_raw} -> Ошибка: {e}")


if __name__ == "__main__":
    main()