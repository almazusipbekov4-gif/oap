import json


def main():
    input_file = "data.txt"
    output_file = "result.json"
    records = []

    try:
        with open(input_file, "r", encoding="utf-8") as f:
            for line_num, raw_line in enumerate(f, start=1):
                line = raw_line.strip()
                if not line:
                    continue

                parts = [p.strip() for p in line.split(";")]
                if len(parts) != 2 or not parts[0]:
                    print(f"Строка {line_num}: неверный формат -> '{line}'")
                    continue

                category, amount_raw = parts
                try:
                    amount = float(amount_raw)
                except ValueError:
                    print(f"Строка {line_num}: некорректная сумма '{amount_raw}'")
                    continue

                records.append({"category": category, "amount": amount})
    except FileNotFoundError:
        print(f"Ошибка: файл '{input_file}' не найден.")
        return

    total_expenses = sum(item["amount"] for item in records)
    top_category = max(records, key=lambda x: x["amount"]) if records else None

    result_data = {
        "records": records,
        "summary": {
            "total_expenses": round(total_expenses, 2),
            "count": len(records),
            "most_expensive_category": top_category["category"] if top_category else None,
            "most_expensive_amount": top_category["amount"] if top_category else 0.0,
        },
    }

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(result_data, f, ensure_ascii=False, indent=2)

    with open(output_file, "r", encoding="utf-8") as f:
        loaded = json.load(f)

    print("=== Сводка (Вариант 6) ===")
    print("Общая сумма расходов:", loaded["summary"]["total_expenses"])
    print("Самая затратная категория:", loaded["summary"]["most_expensive_category"], loaded["summary"]["most_expensive_amount"])


if __name__ == "__main__":
    main()