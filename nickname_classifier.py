import json
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Embedding, LSTM, Dropout
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences


# Загрузка данных
with open('train_categorized_nicknames.json', 'r', encoding='utf-8') as f:
    train_data = json.load(f)["train_set"]

with open('categorized_nicknames.json', 'r', encoding='utf-8') as f:
    categories = json.load(f)


# Подготовка данных
nicknames = []
labels = []

for category, names in categories.items():
    nicknames.extend(names)
    labels.extend([category] * len(names))

# Токенизация
tokenizer = Tokenizer()
tokenizer.fit_on_texts(nicknames)

X = tokenizer.texts_to_sequences(nicknames)
X = pad_sequences(X, padding='post')

# Преобразование меток в числовой формат
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(labels)

# Разделение на обучающую и тестовую выборки
X_train, X_val, y_train, y_val = train_test_split(
    X, y, test_size=0.2, random_state=42)

# Построение модели
model = Sequential([
    Embedding(
        input_dim=len(tokenizer.word_index) + 1,
        output_dim=64, input_length=X.shape[1]),
    LSTM(128, return_sequences=True),
    Dropout(0.5),
    LSTM(64),
    Dropout(0.5),
    Dense(64, activation='relu'),
    Dense(len(set(labels)), activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Обучение модели
history = model.fit(
    X_train, y_train,
    validation_data=(X_val, y_val),
    epochs=10,
    batch_size=32
)

# Сохранение модели и токенайзера
model.save('nickname_classifier.h5')
with open('tokenizer.json', 'w') as f:
    json.dump(tokenizer.to_json(), f)

# Проверка на тестовом наборе
def classify_nickname(nickname):
    seq = tokenizer.texts_to_sequences([nickname])
    seq = pad_sequences(seq, maxlen=X.shape[1], padding='post')
    pred = model.predict(seq)
    return label_encoder.inverse_transform([np.argmax(pred)])[0]

# Пример использования
print(classify_nickname("ToToRo"))

