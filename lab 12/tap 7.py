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

                participant, time_raw = parts
                try:
                    time_val = float(time_raw)
                except ValueError:
                    print(f"Строка {line_num}: некорректное время '{time_raw}'")
                    continue

                records.append({"participant": participant, "time": time_val})
    except FileNotFoundError:
        print(f"Ошибка: файл '{input_file}' не найден.")
        return

    count = len(records)
    average_time = sum(item["time"] for item in records) / count if count > 0 else 0.0
    best_record = min(records, key=lambda x: x["time"]) if records else None

    result_data = {
        "records": records,
        "summary": {
            "average_time": round(average_time, 2),
            "count": count,
            "best_time": best_record["time"] if best_record else None,
            "best_participant": best_record["participant"] if best_record else None,
        },
    }

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(result_data, f, ensure_ascii=False, indent=2)

    with open(output_file, "r", encoding="utf-8") as f:
        loaded = json.load(f)

    print("=== Сводка (Вариант 7) ===")
    print("Среднее время:", loaded["summary"]["average_time"])
    print("Лучшее время:", loaded["summary"]["best_time"], f"({loaded['summary']['best_participant']})")


if __name__ == "__main__":
    main()