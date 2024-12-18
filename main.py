import json
from datetime import datetime

# Пути к файлам
input_file = 'user_names.json'
output_file = 'filtered_user_names.json'

try:
    # Чтение исходного JSON-файла
    with open(input_file, 'r', encoding='utf-8') as file:
        data = json.load(file)

    if isinstance(data, list):
        initial_count = len(data)

        # Счётчики удалений по каждому полю
        empty_first_name_count = 0
        empty_last_name_count = 0
        empty_nickname_count = 0

        # Фильтрация записей и добавление производных данных
        filtered_data = []
        for item in data:
            # Проверяем пустые поля
            first_name = item.get('first_name')
            last_name = item.get('last_name')
            nickname = item.get('nickname')

            # Увеличиваем счётчики, если поле пустое
            if not first_name:
                empty_first_name_count += 1
            if not last_name:
                empty_last_name_count += 1
            if not nickname:
                empty_nickname_count += 1

            # Пропускаем запись, если хотя бы одно поле пустое
            if not first_name or not last_name or not nickname:
                continue

            # Обрабатываем full_name
            first_name = first_name.strip() if isinstance(first_name, str) else ''
            last_name = last_name.strip() if isinstance(last_name, str) else ''
            item['full_name'] = f"{first_name} {last_name}".strip()

            # Обрабатываем временные данные
            downloaded_at = item.get('downloaded_at', {}).get('$date')
            if downloaded_at:
                try:
                    downloaded_date = datetime.strptime(downloaded_at, "%Y-%m-%dT%H:%M:%S.%fZ")
                    item['year_downloaded'] = downloaded_date.year
                    item['month_downloaded'] = downloaded_date.month
                    item['day_downloaded'] = downloaded_date.day
                except ValueError:
                    item['year_downloaded'] = None
                    item['month_downloaded'] = None
                    item['day_downloaded'] = None
            else:
                item['year_downloaded'] = None
                item['month_downloaded'] = None
                item['day_downloaded'] = None

            # Добавляем запись в список, если она прошла все проверки
            filtered_data.append(item)

        final_count = len(filtered_data)
        removed_count = initial_count - final_count

        # Запись отфильтрованных данных с производными полями в новый файл
        with open(output_file, 'w', encoding='utf-8') as out_file:
            json.dump(filtered_data, out_file, ensure_ascii=False, indent=4)

        # Вывод статистики
        print(f"Обработано записей: {initial_count}")
        print(f"Удалено записей: {removed_count}")
        print(f"  - Пустое поле 'first_name': {empty_first_name_count}")
        print(f"  - Пустое поле 'last_name': {empty_last_name_count}")
        print(f"  - Пустое поле 'nickname': {empty_nickname_count}")
        print(f"Результат сохранён в файл: {output_file}")
    else:
        print("Ожидается массив объектов в JSON.")

except FileNotFoundError:
    print(f"Файл {input_file} не найден.")
except json.JSONDecodeError as e:
    print(f"Ошибка при разборе JSON: {e}")
