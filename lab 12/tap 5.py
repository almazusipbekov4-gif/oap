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

                title, year_raw = parts
                try:
                    year = int(year_raw)
                except ValueError:
                    print(f"Строка {line_num}: некорректный год '{year_raw}'")
                    continue

                records.append({"title": title, "year": year})
    except FileNotFoundError:
        print(f"Ошибка: файл '{input_file}' не найден.")
        return

    books_count = len(records)
    earliest_year = min((item["year"] for item in records), default=None)
    after_2020_count = sum(1 for item in records if item["year"] > 2020)

    result_data = {
        "records": records,
        "summary": {
            "books_count": books_count,
            "earliest_year": earliest_year,
            "after_2020_count": after_2020_count,
        },
    }

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(result_data, f, ensure_ascii=False, indent=2)

    with open(output_file, "r", encoding="utf-8") as f:
        loaded = json.load(f)

    print("=== Сводка (Вариант 5) ===")
    print("Число книг:", loaded["summary"]["books_count"])
    print("Самый ранний год:", loaded["summary"]["earliest_year"])
    print("Книг после 2020 года:", loaded["summary"]["after_2020_count"])


if __name__ == "__main__":
    main()