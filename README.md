# 🎓 University DB — Домашнє завдання GOIT Python Web HW6

## 📦 Опис

Цей проєкт реалізує повноцінну базу даних для університету з використанням:

- PostgreSQL (через Docker)
- SQLAlchemy ORM
- Alembic (міграції)
- Faker (для генерації фейкових даних)
- Select-запити для роботи з даними

---

## 📁 Структура проєкту

goit-pythonweb-hw-06/ │ ├── models.py # ORM-моделі ├── database.py # Підключення до БД ├── seed.py # Заповнення фейковими даними ├── my_select.py # SQL-запити ├── alembic/ # Міграції Alembic ├── alembic.ini # Налаштування Alembic └── README.md 

## 🚀 Як запустити

### 1. 🔧 Встановити залежності

pip install sqlalchemy psycopg2-binary alembic faker

### 2. 🐳 Запустити PostgreSQL через Docker

docker run --name my_university_db_alt \
  -p 5433:5432 \
  -e POSTGRES_PASSWORD=mysecretpassword \
  -d postgres

### 3. 🧱 Створити базу вручну

docker exec -it my_university_db_alt psql -U postgres

#### Усередині PostgreSQL':'

CREATE DATABASE university;
\q

### 4. 🛠️ Alembic — міграції

alembic init alembic

#### налаштувати alembic.ini + env.py

alembic revision --autogenerate -m "Initial schema"
alembic upgrade head

### 5. 🌱 Заповнення бази

python seed.py

### 6. 📊 Виконання запитів

python my_select.py

Можна викликати будь-яку функцію: select_1(), select_2("Math"), тощо

#### ✅ Запити (select_X)':'

Топ-5 студентів з найвищим середнім
Студент з найвищим балом по предмету
Середній бал по групах з предмету
Середній бал по всіх оцінках
Курси певного викладача
Студенти певної групи
Оцінки студентів групи з предмету
Середній бал, який ставить викладач
Курси, які відвідує студент
Курси, які читає викладач цьому студенту

👩‍💻 Автор: Lesya Katanova
