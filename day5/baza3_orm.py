# Mapowanie obiektowo-relacyjne (ang. Object-Relational Mapping – ORM) – sposób odwzorowania
# obiektowej architektury systemu informatycznego na bazę danych (lub inny element systemu)
# o relacyjnym charakterze.

# sqlalchemy, pewee
# django orm

# pip install sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)


engine = create_engine('sqlite:///my_database.db', echo=True)

Base.metadata.create_all(engine)
# CREATE TABLE users (
# 	id INTEGER NOT NULL,
# 	name VARCHAR,
# 	age INTEGER,
# 	PRIMARY KEY (id)
# )

Session = sessionmaker(bind=engine)
session = Session()

new_user = User(name="Jan", age=30)
session.add(new_user)
session.commit()  # INSERT INTO users (name, age) VALUES (?, ?)

#  SELECT users.id AS users_id, users.name AS users_name, users.age AS users_age
# FROM users
users = session.query(User).all()

for u in users:
    print(u.name)
# Jan
# Jan
