price = 1000
discount = 15
print(price - discount)

def calc_discounted_price(price: float, discount: float) -> float:
    if price < 0:
        raise ValueError("Цена не может быть отрицательной.")
    if not (0 <= discount <= 100):
        raise ValueError("Скидка должна быть в диапазоне от 0 до 100.")
    return price * (1 - discount / 100)


def main():
    cases = [
        (1000, 15),
        (500, 0),
        (500, 120),
        (500, 100),  # дополнительный граничный тест: скидка 100% -> 0.0
    ]

    for price, discount in cases:
        try:
            result = calc_discounted_price(price, discount)
            print(f"Цена={price}, скидка={discount}% -> Итого: {result:.1f}")
        except ValueError as e:
            print(f"Цена={price}, скидка={discount}% -> Ошибка: {e}")


if __name__ == "__main__":
    main()