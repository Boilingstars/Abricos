import sqlite3
from datetime import datetime

# Создание или подключение к базе данных
conn = sqlite3.connect('goods_manager_db.sqlite3')

# Создание курсора для выполнения SQL-запросов
cursor = conn.cursor()

# Создание таблицы с указанными полями
cursor.execute('''
CREATE TABLE IF NOT EXISTS Tables_goods (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price REAL NOT NULL,
    category TEXT NOT NULL,
    markets TEXT NOT NULL,
    date TEXT NOT NULL,
    published BOOLEAN NOT NULL  -- Добавлено поле published
)
''')

# Данные для вставки
name = "Смарт часы X Series, умные часы 45 mm, мужские, женские"
price = 1200
goods_category = "Смарт-часы"
markets = "Ozon"  # Список из строк, но в SQLite мы будем хранить его как строку
date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Текущая дата и время
published = True

# Вставка данных в таблицу
cursor.execute('''
INSERT INTO Tables_goods (name, price, goods_category, markets, date, published) VALUES (?, ?, ?, ?, ?, ?)
''', (name, price, goods_category, markets, date, published))

# Сохранение изменений
conn.commit()

# Закрытие соединения
conn.close()

print("База данных и таблица успешно созданы, данные добавлены.")