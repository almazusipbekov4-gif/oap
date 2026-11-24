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

                name, score_raw = parts
                try:
                    score = float(score_raw)
                except ValueError:
                    print(f"Строка {line_num}: некорректный балл '{score_raw}'")
                    continue

                records.append({"name": name, "score": score})
    except FileNotFoundError:
        print(f"Ошибка: файл '{input_file}' не найден.")
        return

    count = len(records)
    average_score = sum(item["score"] for item in records) / count if count > 0 else 0.0
    max_score = max((item["score"] for item in records), default=None)
    best_students = [item["name"] for item in records if item["score"] == max_score] if max_score is not None else []

    result_data = {
        "records": records,
        "summary": {
            "average_score": round(average_score, 2),
            "count": count,
            "best_score": max_score,
            "best_students": best_students,
        },
    }

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(result_data, f, ensure_ascii=False, indent=2)

    with open(output_file, "r", encoding="utf-8") as f:
        loaded = json.load(f)

    print("=== Сводка (Вариант 1) ===")
    print("Число результатов:", loaded["summary"]["count"])
    print("Средний балл:", loaded["summary"]["average_score"])
    print("Лучший балл:", loaded["summary"]["best_score"], "| Лучшие:", ", ".join(loaded["summary"]["best_students"]))


if __name__ == "__main__":
    main()