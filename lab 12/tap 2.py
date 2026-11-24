import json


def main():
    input_file = "data.txt"
    output_file = "result.json"
    threshold = 23.0  # порог для дополнительного задания
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

                sensor, temp_raw = parts
                try:
                    temperature = float(temp_raw)
                except ValueError:
                    print(f"Строка {line_num}: некорректная температура '{temp_raw}'")
                    continue

                records.append({"sensor": sensor, "temperature": temperature})
    except FileNotFoundError:
        print(f"Ошибка: файл '{input_file}' не найден.")
        return

    count = len(records)
    avg_temp = sum(item["temperature"] for item in records) / count if count > 0 else 0.0
    above_threshold = [item for item in records if item["temperature"] > threshold]

    result_data = {
        "records": records,
        "summary": {
            "average_temperature": round(avg_temp, 2),
            "count": count,
            "threshold": threshold,
            "above_threshold": above_threshold,
        },
    }

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(result_data, f, ensure_ascii=False, indent=2)

    with open(output_file, "r", encoding="utf-8") as f:
        loaded = json.load(f)

    print("=== Сводка (Вариант 2) ===")
    print("Число записей:", loaded["summary"]["count"])
    print("Средняя температура:", loaded["summary"]["average_temperature"])
    print(f"Выше порога ({threshold}):", [f"{x['sensor']} ({x['temperature']})" for x in loaded["summary"]["above_threshold"]])


if __name__ == "__main__":
    main()