from sqlalchemy import func, desc
from database import Session
from models import Student, Grade, Subject, Teacher, Group

session = Session()

# 1. Топ-5 студентів із найбільшим середнім балом
def select_1():
    return session.query(
        Student.full_name,
        func.round(func.avg(Grade.grade), 2).label("avg_grade")
    ).join(Grade).group_by(Student.id).order_by(desc("avg_grade")).limit(5).all()

# 2. Студент з найвищим середнім по предмету
def select_2(subject_name):
    return session.query(
        Student.full_name,
        func.round(func.avg(Grade.grade), 2).label("avg_grade")
    ).join(Grade).join(Subject).filter(Subject.name == subject_name).group_by(Student.id)\
     .order_by(desc("avg_grade")).limit(1).first()

# 3. Середній бал у групах з певного предмета
def select_3(subject_name):
    return session.query(
        Group.name,
        func.round(func.avg(Grade.grade), 2).label("avg_grade")
    ).join(Student).join(Grade).join(Subject)\
     .filter(Subject.name == subject_name).group_by(Group.id).all()

# 4. Середній бал по всій таблиці оцінок
def select_4():
    return session.query(func.round(func.avg(Grade.grade), 2)).scalar()

# 5. Курси, які читає певний викладач
def select_5(teacher_name):
    return session.query(Subject.name).join(Teacher)\
        .filter(Teacher.full_name == teacher_name).all()

# 6. Студенти певної групи
def select_6(group_name):
    return session.query(Student.full_name).join(Group)\
        .filter(Group.name == group_name).all()

# 7. Оцінки студентів у групі з предмета
def select_7(group_name, subject_name):
    return session.query(
        Student.full_name,
        Grade.grade
    ).join(Group).join(Grade).join(Subject)\
     .filter(Group.name == group_name, Subject.name == subject_name).all()

# 8. Середній бал, який ставить певний викладач
def select_8(teacher_name):
    return session.query(func.round(func.avg(Grade.grade), 2))\
        .join(Subject).join(Teacher)\
        .filter(Teacher.full_name == teacher_name).scalar()

# 9. Курси, які відвідує певний студент
def select_9(student_name):
    return session.query(Subject.name).join(Grade).join(Student)\
        .filter(Student.full_name == student_name).distinct().all()

# 10. Курси, які певному студенту читає певний викладач
def select_10(student_name, teacher_name):
    return session.query(Subject.name).join(Teacher).join(Grade).join(Student)\
        .filter(Student.full_name == student_name, Teacher.full_name == teacher_name).distinct().all()

if __name__ == "__main__":
    print("Top 5 students:", select_1())
    # print("Найкращий студент з предмета:", select_2("Math"))
    # print("Середній бал по групах з предмета:", select_3("Math"))
    # print("Середній бал по потоку:", select_4())
