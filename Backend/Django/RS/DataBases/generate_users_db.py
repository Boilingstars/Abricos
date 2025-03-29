import sqlite3

# Создание или подключение к базе данных
conn = sqlite3.connect('users_manager_db.sqlite3')

# Создание курсора для выполнения SQL-запросов
cursor = conn.cursor()

# Создание таблицы с указанными полями
cursor.execute('''
CREATE TABLE IF NOT EXISTS all_users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT NOT NULL,
    login TEXT NOT NULL,
    password TEXT NOT NULL,
    key TEXT NOT NULL
)
''')

# Данные для вставки
data = ('example1@somemail.com', 'login1', '123qwe', '123q-123w-123e')

# Вставка данных в таблицу
cursor.execute('''
INSERT INTO all_users (email, login, password, key) VALUES (?, ?, ?, ?)
''', data)

# Сохранение изменений
conn.commit()

# Закрытие соединения
conn.close()

print("База данных и таблица успешно созданы, данные добавлены.")