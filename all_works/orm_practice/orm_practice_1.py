from sqlalchemy import create_engine, Column, Integer, String, or_, and_, not_, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine("postgresql://owner_orm_practice:owner_orm_practice@localhost:5432/orm_practice")
Session = sessionmaker(bind=engine)
session = Session()

BASE = declarative_base()


class Student(BASE):
    __tablename__ = "student"
    ID = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)
    grade = Column(String(50))


class StudentFriends(BASE):
    __tablename__ = "student_friends"

    ID = Column(Integer, primary_key=True)
    owner_friends_id = Column(Integer, ForeignKey("student.ID"))
    friend_name = Column(String(100))


class Teachers(BASE):
    __tablename__ = "teachers"

    ID = relationship(Integer, primary_key=True)
    name = Column(String(100))


class TeacherFriends(BASE):
    __tablename__ = "teacher_friends"

    ID = Column(Integer, primary_key=True)
    teacher_id = relationship("teachers")

# BASE.metadata.create_all(engine)
# student_1 = StudentFriends(owner_friends_id=6, friend_name="shamsiya")
# student_2 = StudentFriends(owner_friends_id=2, friend_name="xushvaqt")
# student_3 = StudentFriends(owner_friends_id=3, friend_name="xusi")
# session.add_all([student_1, student_2, student_3])
# session.commit()

# students = session.query(Student)
# for i in students:
#     print(i.ID, i.name, i.age, i.grade)

# students = session.query(Student).order_by(Student.name)
# for i in students:
#     print(i.name)

# students = session.query(Student).filter(and_(Student.name == "nargiza", Student.ID == 3)).all()
# for i in students:
#     print(i.ID, i.name)

# students = session.query(Student).filter(or_(Student.name == "nargiza", Student.name == "oydin")).all()
# for i in students:
#     print(i.ID, i.name)

# students = session.query(Student).filter(or_(Student.name == "nargiza", Student.name == "oydin")).count()
# print(students)

# student_change = session.query(Student).filter(Student.name == "ozod").all()
# for i in student_change:
#     i.name = "ozod ochilboyev"
#     session.commit()
# student_change = session.query(Student)
# for i in student_change:
#     print(i.ID, i.name)

# student_change = session.query(Student).filter(Student.name == "ozod ochilboyev").first()
# print(student_change.ID, student_change.name)
# session.delete(student_change)
# session.commit()
