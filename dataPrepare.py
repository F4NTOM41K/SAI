import json
import pandas as pd
from sklearn.model_selection import train_test_split

# Загрузка данных из файла
file_path = 'categorized.json'
with open(file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

# Преобразование данных в DataFrame
categories = ['frenonim', 'titlonim', 'etnonim', 'incognitonim']
rows = [(nickname, category) for category in categories for nickname in data[category]]
df = pd.DataFrame(rows, columns=['nickname', 'category'])

# Разделение на тренировочный и тестовый наборы (80/20)
train_set, test_set = train_test_split(df, test_size=0.2, random_state=42, stratify=df['category'])

# Вывод размеров наборов
train_set_size = train_set.shape[0]
test_set_size = test_set.shape[0]

# Сохранение в CSV для удобства
train_set_path = 'data/train_set.csv'
test_set_path = 'data/test_set.csv'
train_set.to_csv(train_set_path, index=False, encoding='utf-8')
test_set.to_csv(test_set_path, index=False, encoding='utf-8')

train_set_path, test_set_path, train_set_size, test_set_size
