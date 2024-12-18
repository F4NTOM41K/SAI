from datetime import datetime

def add_full_name(item):
    """
    Добавляет поле full_name (полное имя).
    """
    first_name = item.get('first_name', '').strip()
    last_name = item.get('last_name', '').strip()
    item['full_name'] = f"{first_name} {last_name}".strip()\
        if first_name and last_name else None

def add_date_fields(item):
    """
    Извлекает год, месяц и день из поля downloaded_at и добавляет их как отдельные поля.
    """
    downloaded_at = item.get('downloaded_at', {}).get('$date')
    if downloaded_at:
        try:
            downloaded_date = datetime.strptime(
                downloaded_at, "%Y-%m-%dT%H:%M:%S.%fZ")
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


def add_user_details(item, users_dict):
    """
    Добавляет дополнительные данные ('sex', 'bdate') из словаря пользователей по id.

    :param item: Словарь с данными записи.
    :param users_dict: Словарь, где ключ - 'id', значение - данные пользователя.
    """
    user_id = item.get('id')
    if user_id and user_id in users_dict:
        user_details = users_dict[user_id]
        item['sex'] = user_details.get('sex')
        item['bdate'] = user_details.get('bdate')
