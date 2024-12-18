from collections import Counter

def count_field_values(data, field):
    """
    Подсчитывает частоту значений в указанном поле.
    """
    values = [item.get(field, '').strip().lower() \
              for item in data if field in item]
    return Counter(values)

def filter_empty_fields(data, required_fields):
    """
    Фильтрует записи, удаляя те, где есть пустые значения в указанных полях.
    """
    filtered_data = []
    empty_counts = {field: 0 for field in required_fields}

    for item in data:
        skip = False
        for field in required_fields:
            if not item.get(field):
                empty_counts[field] += 1
                skip = True
        if not skip:
            filtered_data.append(item)

    return filtered_data, empty_counts
