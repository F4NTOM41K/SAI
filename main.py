from data_analysis.file_io import load_json, save_json
from data_analysis.transformations import add_full_name, add_date_fields, add_user_details
from data_analysis.analysis import filter_empty_fields, count_field_values


def main():
    # Пути к файлам
    input_file = 'user_names.json'  # Основной файл
    users_file = 'users.json'  # Файл с дополнительной информацией о пользователях
    output_file = 'filtered_user_names.json'  # Итоговый файл

    # Чтение данных из файлов
    print("Чтение данных...")
    data = load_json(input_file)
    users_data = load_json(users_file)

    if data is None or users_data is None:
        print("Не удалось загрузить данные.")
        return

    # Проверка, что данные являются списками
    if not isinstance(data, list) or not isinstance(users_data, list):
        print("Ошибка: данные должны быть массивами объектов (списками).")
        return

    # Создание словаря пользователей для быстрого поиска
    print("Создание словаря пользователей...")
    users_dict = {user['id']: user for user in users_data if 'id' in user}

    # Фильтрация записей с пустыми полями
    print("Фильтрация данных...")
    required_fields = ['first_name', 'last_name', 'nickname']
    filtered_data, empty_counts = filter_empty_fields(data, required_fields)

    # Добавление производных данных
    print("Добавление производных данных...")
    for item in filtered_data:
        add_full_name(item)  # Добавление полного имени
        add_date_fields(item)  # Извлечение временных данных
        add_user_details(item, users_dict)  # Добавление пола и даты рождения

        # Отладочная информация
        if item.get('sex') or item.get('bdate'):
            print(
                f"ID {item.get('id')}: Пол - {item.get('sex')}, День рождения - {item.get('bdate')}")

    # Сохранение обработанных данных в новый файл
    print("Сохранение обработанных данных...")
    save_json(filtered_data, output_file)

    # Анализ данных: частотность никнеймов
    print("Анализ данных...")
    nickname_frequencies = count_field_values(filtered_data, 'nickname')

    # Вывод статистики
    print("\nСтатистика обработки:")
    print(f"Обработано записей: {len(data)}")
    print(f"Удалено записей: {len(data) - len(filtered_data)}")
    for field, count in empty_counts.items():
        print(f"  - Пустое поле '{field}': {count}")

    print("\nЧастотность никнеймов (топ-10):")
    for nickname, freq in nickname_frequencies.most_common(10):
        print(f"  {nickname}: {freq}")

    print(f"\nОбработанные данные сохранены в файл: {output_file}")


# Запуск программы
if __name__ == "__main__":
    main()



# import json
# from datetime import datetime
#
# # Пути к файлам
# input_file = 'user_names.json'
# output_file = 'filtered_user_names.json'
#
# try:
#     # Чтение исходного JSON-файла
#     with open(input_file, 'r', encoding='utf-8') as file:
#         data = json.load(file)
#
#     if isinstance(data, list):
#         initial_count = len(data)
#
#         # Счётчики удалений по каждому полю
#         empty_first_name_count = 0
#         empty_last_name_count = 0
#         empty_nickname_count = 0
#
#         # Фильтрация записей и добавление производных данных
#         filtered_data = []
#         for item in data:
#             # Проверяем пустые поля
#             first_name = item.get('first_name')
#             last_name = item.get('last_name')
#             nickname = item.get('nickname')
#
#             # Увеличиваем счётчики, если поле пустое
#             if not first_name:
#                 empty_first_name_count += 1
#             if not last_name:
#                 empty_last_name_count += 1
#             if not nickname:
#                 empty_nickname_count += 1
#
#             # Пропускаем запись, если хотя бы одно поле пустое
#             if not first_name or not last_name or not nickname:
#                 continue
#
#             # Обрабатываем full_name
#             first_name = first_name.strip() if isinstance(first_name, str) else ''
#             last_name = last_name.strip() if isinstance(last_name, str) else ''
#             item['full_name'] = f"{first_name} {last_name}".strip()
#
#             # Обрабатываем временные данные
#             downloaded_at = item.get('downloaded_at', {}).get('$date')
#             if downloaded_at:
#                 try:
#                     downloaded_date = datetime.strptime(downloaded_at, "%Y-%m-%dT%H:%M:%S.%fZ")
#                     item['year_downloaded'] = downloaded_date.year
#                     item['month_downloaded'] = downloaded_date.month
#                     item['day_downloaded'] = downloaded_date.day
#                 except ValueError:
#                     item['year_downloaded'] = None
#                     item['month_downloaded'] = None
#                     item['day_downloaded'] = None
#             else:
#                 item['year_downloaded'] = None
#                 item['month_downloaded'] = None
#                 item['day_downloaded'] = None
#
#             # Добавляем запись в список, если она прошла все проверки
#             filtered_data.append(item)
#
#         final_count = len(filtered_data)
#         removed_count = initial_count - final_count
#
#         # Запись отфильтрованных данных с производными полями в новый файл
#         with open(output_file, 'w', encoding='utf-8') as out_file:
#             json.dump(filtered_data, out_file, ensure_ascii=False, indent=4)
#
#         # Вывод статистики
#         print(f"Обработано записей: {initial_count}")
#         print(f"Удалено записей: {removed_count}")
#         print(f"  - Пустое поле 'first_name': {empty_first_name_count}")
#         print(f"  - Пустое поле 'last_name': {empty_last_name_count}")
#         print(f"  - Пустое поле 'nickname': {empty_nickname_count}")
#         print(f"Результат сохранён в файл: {output_file}")
#     else:
#         print("Ожидается массив объектов в JSON.")
#
# except FileNotFoundError:
#     print(f"Файл {input_file} не найден.")
# except json.JSONDecodeError as e:
#     print(f"Ошибка при разборе JSON: {e}")
