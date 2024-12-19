import json
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

# Загрузка данных из файла
file_path = 'data/augmented_train_set.csv'  # Укажите путь к вашему файлу
train_set = pd.read_csv(file_path)

# Преобразование данных в DataFrame
categories = ['frenonim', 'titlonim', 'etnonim', 'incognitonim']

# Разделение на тренировочный и тестовый наборы (80/20)
original_file_path = 'categorized.json'  # Исходный файл для теста
with open(original_file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)
rows = [(nickname, category) for category in categories for nickname in data[category]]
test_set = pd.DataFrame(rows, columns=['nickname', 'category'])

# Преобразование данных в TF-IDF формат
tfidf_vectorizer = TfidfVectorizer(analyzer='char', ngram_range=(2, 4), max_features=5000)
X_train = tfidf_vectorizer.fit_transform(train_set['nickname'])
X_test = tfidf_vectorizer.transform(test_set['nickname'])

# Целевые метки
y_train = train_set['category']
y_test = test_set['category']

# Обучение модели
model = LogisticRegression(random_state=42, max_iter=1000)
model.fit(X_train, y_train)

# Предсказания и отчет
y_pred = model.predict(X_test)
classification_rep = classification_report(y_test, y_pred, target_names=categories)

# Вывод отчета
print("Классификация никнеймов:")
print(classification_rep)

# Сохранение модели и векторизатора для последующего использования
import joblib
model_path = 'nickname_classifier_model_augmented.pkl'
vectorizer_path = 'nickname_vectorizer_augmented.pkl'
joblib.dump(model, model_path)
joblib.dump(tfidf_vectorizer, vectorizer_path)

print(f"Модель сохранена в {model_path}")
print(f"Векторизатор сохранен в {vectorizer_path}")
