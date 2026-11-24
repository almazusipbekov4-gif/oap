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

                device, kwh_raw = parts
                try:
                    kwh = float(kwh_raw)
                except ValueError:
                    print(f"Строка {line_num}: некорректное значение кВтч '{kwh_raw}'")
                    continue

                records.append({"device": device, "kwh": kwh})
    except FileNotFoundError:
        print(f"Ошибка: файл '{input_file}' не найден.")
        return

    total_kwh = sum(item["kwh"] for item in records)
    max_device = max(records, key=lambda x: x["kwh"]) if records else None

    result_data = {
        "records": records,
        "summary": {
            "total_kwh": round(total_kwh, 2),
            "count": len(records),
            "max_consumption_device": max_device["device"] if max_device else None,
            "max_kwh": max_device["kwh"] if max_device else 0.0,
        },
    }

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(result_data, f, ensure_ascii=False, indent=2)

    with open(output_file, "r", encoding="utf-8") as f:
        loaded = json.load(f)

    print("=== Сводка (Вариант 9) ===")
    print("Общий расход энергии (кВтч):", loaded["summary"]["total_kwh"])
    print("Прибор с максимальным расходом:", loaded["summary"]["max_consumption_device"], loaded["summary"]["max_kwh"])


if __name__ == "__main__":
    main()