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

                route, minutes_raw = parts
                try:
                    minutes = float(minutes_raw)
                except ValueError:
                    print(f"Строка {line_num}: некорректная длительность '{minutes_raw}'")
                    continue

                records.append({"route": route, "minutes": minutes})
    except FileNotFoundError:
        print(f"Ошибка: файл '{input_file}' не найден.")
        return

    count = len(records)
    average_minutes = sum(item["minutes"] for item in records) / count if count > 0 else 0.0
    over_30_count = sum(1 for item in records if item["minutes"] > 30)

    result_data = {
        "records": records,
        "summary": {
            "average_minutes": round(average_minutes, 2),
            "count": count,
            "trips_over_30_min": over_30_count,
        },
    }

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(result_data, f, ensure_ascii=False, indent=2)

    with open(output_file, "r", encoding="utf-8") as f:
        loaded = json.load(f)

    print("=== Сводка (Вариант 10) ===")
    print("Средняя длительность (мин):", loaded["summary"]["average_minutes"])
    print("Поездок дольше 30 минут:", loaded["summary"]["trips_over_30_min"])


if __name__ == "__main__":
    main()