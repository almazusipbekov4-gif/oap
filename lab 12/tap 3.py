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
                if len(parts) != 3 or not parts[0]:
                    print(f"Строка {line_num}: неверный формат -> '{line}'")
                    continue

                product, qty_raw, price_raw = parts
                try:
                    quantity = int(qty_raw)
                    price = float(price_raw)
                except ValueError:
                    print(f"Строка {line_num}: некорректные числа '{qty_raw}', '{price_raw}'")
                    continue

                revenue = quantity * price
                records.append({
                    "product": product,
                    "quantity": quantity,
                    "price": price,
                    "revenue": revenue,
                })
    except FileNotFoundError:
        print(f"Ошибка: файл '{input_file}' не найден.")
        return

    total_revenue = sum(item["revenue"] for item in records)
    top_item = max(records, key=lambda x: x["revenue"]) if records else None

    result_data = {
        "records": records,
        "summary": {
            "total_revenue": round(total_revenue, 2),
            "count": len(records),
            "top_revenue_product": top_item["product"] if top_item else None,
            "top_revenue": top_item["revenue"] if top_item else 0.0,
        },
    }

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(result_data, f, ensure_ascii=False, indent=2)

    with open(output_file, "r", encoding="utf-8") as f:
        loaded = json.load(f)

    print("=== Сводка (Вариант 3) ===")
    print("Суммарная выручка:", loaded["summary"]["total_revenue"])
    print("Товар с максимальной выручкой:", loaded["summary"]["top_revenue_product"], loaded["summary"]["top_revenue"])


if __name__ == "__main__":
    main()