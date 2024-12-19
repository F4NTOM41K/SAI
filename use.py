import joblib

# Загрузка обученной модели и TF-IDF векторизатора
model_path = 'nickname_classifier_model_augmented.pkl'
vectorizer_path = 'nickname_vectorizer_augmented.pkl'

# Загрузка модели и векторизатора
model = joblib.load(model_path)
vectorizer = joblib.load(vectorizer_path)

def predict_category(nickname):
    """Функция для предсказания категории никнейма."""
    nickname_transformed = vectorizer.transform([nickname])
    predicted_category = model.predict(nickname_transformed)[0]
    return predicted_category

# Пример использования
example_nickname = "Cock"
predicted = predict_category(example_nickname)
print(f"Никнейм: {example_nickname}, Категория: {predicted}")