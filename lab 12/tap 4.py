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

                group, present_raw, total_raw = parts
                try:
                    present = int(present_raw)
                    total = int(total_raw)
                except ValueError:
                    print(f"Строка {line_num}: некорректные числа '{present_raw}', '{total_raw}'")
                    continue

                if total <= 0:
                    print(f"Строка {line_num}: общее число студентов должно быть > 0")
                    continue

                attendance_pct = round((present / total) * 100, 2)
                records.append({
                    "group": group,
                    "present": present,
                    "total": total,
                    "attendance_percent": attendance_pct,
                })
    except FileNotFoundError:
        print(f"Ошибка: файл '{input_file}' не найден.")
        return

    total_present = sum(item["present"] for item in records)
    total_students = sum(item["total"] for item in records)
    overall_pct = round((total_present / total_students) * 100, 2) if total_students > 0 else 0.0
    below_75 = [item for item in records if item["attendance_percent"] < 75.0]

    result_data = {
        "records": records,
        "summary": {
            "attendance_percent": overall_pct,
            "groups_count": len(records),
            "groups_below_75": below_75,
        },
    }

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(result_data, f, ensure_ascii=False, indent=2)

    with open(output_file, "r", encoding="utf-8") as f:
        loaded = json.load(f)

    print("=== Сводка (Вариант 4) ===")
    print("Процент посещаемости:", f"{loaded['summary']['attendance_percent']}%")
    print("Группы ниже 75%:", [f"{g['group']} ({g['attendance_percent']}%)" for g in loaded["summary"]["groups_below_75"]])


if __name__ == "__main__":
    main()