import json
from tabulate import tabulate

# Указываем путь к JSON-файлу
file_path = 'filtered_user_names.json'

# Читаем JSON-файл
try:
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Проверяем, является ли объект списком (массив объектов)
    if isinstance(data, list):
        # Формируем данные для табуляции
        table_data = []
        for item in data:
            table_data.append([
                item.get('full_name', 'N/A'),
                item.get('nickname', 'N/A'),
                item.get('year_downloaded', 'N/A'),
                item.get('month_downloaded', 'N/A'),
                item.get('day_downloaded', 'N/A'),
                item.get('downloaded_at', {}).get('$date', 'N/A')
            ])

        # Определяем заголовки таблицы
        headers = ['Full Name',
                   'Nickname',
                   'Year',
                   'Month',
                   'Day',
                   'Downloaded At']

        # Выводим таблицу
        print(tabulate(table_data, headers=headers, tablefmt='grid'))
    else:
        print("Ожидается массив объектов в JSON.")

except FileNotFoundError:
    print(f"Файл {file_path} не найден.")
except json.JSONDecodeError as e:
    print(f"Ошибка при разборе JSON: {e}")
