from .database import db
from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship


class Department(db.Model):
    __tablename__ = "department"
    id = Column(Integer, primary_key=True)
    code = Column(String(3), unique=True, nullable=False)
    name = Column(String(150), nullable=False)
    supervisors = relationship("Supervisor", back_populates="department")
    topics = relationship("Topic", back_populates="department")


class Supervisor(db.Model):
    __tablename__ = "supervisor"
    id = Column(Integer, primary_key=True)
    staff_id = Column(String(20), unique=True, nullable=False)
    fullname = Column(String(120), nullable=False)
    department_id = Column(Integer, ForeignKey("department.id"))
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    department = relationship("Supervisor", back_populates="supervisors")
    students = relationship("Student", back_populates="supervisor")


class Student(db.Model):
    __tablename__ = "student"
    id = Column(Integer, primary_key=True)
    department_id = Column(Integer, ForeignKey("department.id"))
    level = Column(String(10), nullable=False)
    program = Column(String(15), nullable=False)
    matric = Column(String(16), unique=True, nullable=False)
    fullname = Column(String(150), nullable=False)
    supervisor_id = Column(Integer, ForeignKey("supervisor.id"))
    topic_id = Column(Integer, ForeignKey("topic.id"))


class Allocation(db.Model):
    __tablename__ = "allocation"
    id = Column(Integer, primary_key=True)
    session = Column(String(10), nullable=False)
    department_id = Column(Integer, ForeignKey("department.id"))
    supervisor_id = Column(Integer, ForeignKey("supervisor.id"))
    student_id = Column(Integer, ForeignKey("student.id"))


# Association Table for Topic--ResearchArea
# Many-To-Many relationship
topic_research_area_assoc = Table(
    "topic_research_area_assoc",
    db.metadata,
    Column("topic_id", ForeignKey("topic.id")),
    Column("research_area_id", ForeignKey("research_area.id")),
)


class Topic(db.Model):
    __tablename__ = "topic"
    id = Column(Integer, primary_key=True)
    topic = Column(String(200), nullable=False)
    category = Column(String(10), nullable=False)
    session = Column(String(10), nullable=False)
    department_id = Column(Integer, ForeignKey("department.id"))
    supervisor_id = Column(Integer, ForeignKey("supervisor.id"))
    students = relationship("Student", backref="topic")
    research_areas = relationship(
        secondary=topic_research_area_assoc, back_populates="topics"
    )
    department = relationship("Department", back_populates="topics")


class ResearchArea(db.Model):
    __tablename__ = "research_area"
    id = Column(Integer, primary_key=True)
    department_id = Column(Integer, ForeignKey("department.id"))
    area_name = Column(String(100), nullable=False)
    topics = relationship(
        secondary=topic_research_area_assoc, back_populates="research_areas"
    )
