import json

# Пути к файлам
input_file = 'user_names.json'
output_file = 'filtered_user_names.json'

try:
    # Чтение исходного JSON-файла
    with open(input_file, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Проверяем, является ли объект списком (массив объектов)
    if isinstance(data, list):
        initial_count = len(data)

        # Счётчики удалений по каждому полю
        empty_first_name_count = 0
        empty_last_name_count = 0
        empty_nickname_count = 0

        # Фильтрация записей
        filtered_data = []
        for item in data:
            first_name = item.get('first_name')
            last_name = item.get('last_name')
            nickname = item.get('nickname')

            # Считаем, если поле пустое
            if not first_name:
                empty_first_name_count += 1
            if not last_name:
                empty_last_name_count += 1
            if not nickname:
                empty_nickname_count += 1

            # Добавляем запись, если все поля заполнены
            if first_name and last_name and nickname:
                filtered_data.append(item)

        # Запись отфильтрованных данных в новый файл
        with open(output_file, 'w', encoding='utf-8') as out_file:
            json.dump(filtered_data, out_file, ensure_ascii=False, indent=4)

        removed_count = initial_count - len(filtered_data)

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
