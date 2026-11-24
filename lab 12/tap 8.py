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

                obj_name, rating_raw = parts
                try:
                    rating = float(rating_raw)
                except ValueError:
                    print(f"Строка {line_num}: некорректная оценка '{rating_raw}'")
                    continue

                records.append({"object": obj_name, "rating": rating})
    except FileNotFoundError:
        print(f"Ошибка: файл '{input_file}' не найден.")
        return

    count = len(records)
    average_rating = sum(item["rating"] for item in records) / count if count > 0 else 0.0
    ge_4_count = sum(1 for item in records if item["rating"] >= 4)

    result_data = {
        "records": records,
        "summary": {
            "average_rating": round(average_rating, 2),
            "count": count,
            "ratings_ge_4_count": ge_4_count,
        },
    }

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(result_data, f, ensure_ascii=False, indent=2)

    with open(output_file, "r", encoding="utf-8") as f:
        loaded = json.load(f)

    print("=== Сводка (Вариант 8) ===")
    print("Средняя оценка:", loaded["summary"]["average_rating"])
    print("Число оценок >= 4:", loaded["summary"]["ratings_ge_4_count"])


if __name__ == "__main__":
    main()