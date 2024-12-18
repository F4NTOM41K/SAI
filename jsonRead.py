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
                item.get('_id', 'N/A'),
                item.get('id', 'N/A'),
                item.get('downloaded_at', 'N/A'),
                item.get('first_name', 'N/A'),
                item.get('last_name', 'N/A'),
                item.get('maiden_name', 'N/A'),
                item.get('nickname', 'N/A'),
                item.get('screen_name', 'N/A'),
                item.get('status', 'N/A')
            ])

        # Определяем заголовки таблицы
        headers = [
            '_ID', 'User ID', 'Downloaded At',
            'First Name', 'Last Name', 'Maiden Name',
            'Nickname', 'Screen Name', 'Status'
        ]

        # Выводим таблицу
        print(tabulate(table_data, headers=headers, tablefmt='grid'))
    else:
        print("Ожидается массив объектов в JSON.")

except FileNotFoundError:
    print(f"Файл {file_path} не найден.")
except json.JSONDecodeError as e:
    print(f"Ошибка при разборе JSON: {e}")
