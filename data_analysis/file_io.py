import json

def load_json(file_path):
    """
    Читает JSON-файл и возвращает данные.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")
        return None
    except json.JSONDecodeError as e:
        print(f"Ошибка при разборе JSON: {e}")
        return None

def save_json(data, file_path):
    """
    Сохраняет данные в JSON-файл.
    """
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
        print(f"Данные сохранены в файл: {file_path}")
