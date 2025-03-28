import random
from datetime import datetime, timedelta

from faker import Faker
from sqlalchemy.orm import Session

from database import Session as DBSession, engine
from models import Group, Student, Teacher, Subject, Grade

fake = Faker()

def seed_data():
    session: Session = DBSession()

    # 🔸 1. Групи
    groups = [Group(name=f"ІП-2{n}") for n in range(1, 4)]
    session.add_all(groups)
    session.commit()

    # 🔸 2. Викладачі
    teachers = [Teacher(full_name=fake.name()) for _ in range(random.randint(3, 5))]
    session.add_all(teachers)
    session.commit()

    # 🔸 3. Предмети
    subjects = [
        Subject(
            name=fake.job(),
            teacher=random.choice(teachers)
        ) for _ in range(random.randint(5, 8))
    ]
    session.add_all(subjects)
    session.commit()

    # 🔸 4. Студенти
    students = []
    for _ in range(random.randint(30, 50)):
        student = Student(
            full_name=fake.name(),
            group=random.choice(groups)
        )
        students.append(student)
    session.add_all(students)
    session.commit()

    # 🔸 5. Оцінки
    grades = []
    for student in students:
        for _ in range(random.randint(10, 20)):
            subject = random.choice(subjects)
            grade = Grade(
                student=student,
                subject=subject,
                grade=random.randint(60, 100),
                date_received=fake.date_between(start_date='-6M', end_date='today')
            )
            grades.append(grade)

    session.add_all(grades)
    session.commit()

    print("✅ Базу успішно заповнено")

if __name__ == "__main__":
    seed_data()
