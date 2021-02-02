from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, and_, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pro_diplom.config_keys import owner_db, db_name, db_password

engine = create_engine(f"postgresql+psycopg2://{owner_db}:{db_password}@localhost:5432/{db_name}")

Session = sessionmaker(bind=engine)
session = Session()

BASE = declarative_base()


class Gender(BASE):
    __tablename__ = "user_gender"

    ID = Column(Integer, primary_key=True)
    title = Column(String(20))


class County(BASE):
    __tablename__ = "user_country"

    ID = Column(Integer, primary_key=True)
    name = Column(String(50))


class Town(BASE):
    __tablename__ = "user_town"

    ID = Column(Integer, primary_key=True)
    name = Column(String)


class Status(BASE):
    __tablename__ = "user_status"

    ID = Column(Integer, primary_key=True)
    name = Column(String)


class AllVkUsers(BASE):
    __tablename__ = "all_vk_users"

    vk_id = Column(Integer, primary_key=True)
    name = Column(String(50))
    surname = Column(String(50))
    gender_id = Column(Integer, ForeignKey("user_gender.ID"))
    country_id = Column(Integer, ForeignKey("user_country.ID"))
    town_id = Column(Integer, ForeignKey("user_country.ID"))
    status_id = Column(Integer, ForeignKey("user_status.ID"))
    is_bot_user = Column(Boolean, default=True)


# BASE.metadata.create_all(engine)

