from sqlalchemy import Column, Integer, String, Text, ForeignKey, Table, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

from sqlalchemy_utils import database_exists, create_database

Base = declarative_base()


class_members_table = Table(
    'class_member',
    Base.metadata,
    Column('class_id', Integer, ForeignKey('class.class_id')),
    Column('member_id', Integer, ForeignKey('member.member_id'))
)


class Club(Base):
    __tablename__ = 'club'
    club_id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(Text)
    members = relationship("Member", cascade="all, delete")
    classes = relationship("Class", cascade="all, delete")


class Class(Base):
    __tablename__ = 'class'
    class_id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(Text)
    club_id = Column(Integer, ForeignKey('club.club_id'))
    club = relationship("Club", back_populates="classes")
    class_members = relationship("Member", secondary=class_members_table)


class Member(Base):
    __tablename__ = 'member'
    member_id = Column(Integer, primary_key=True)
    firstname = Column(String)
    lastname = Column(String)
    club_Id = Column(Integer, ForeignKey('club.club_id'))
    club = relationship("Club", back_populates="members")


engine = create_engine('sqlite:///club.db')
Session = sessionmaker(bind=engine)


def create_db():
    if not database_exists(engine.url):
        create_database(engine.url)
        Base.metadata.create_all(engine)
        ClubDAO.insert_default_club()
    else:
        Base.metadata.bind = engine

class MembersDAO:
    model = Member

    @staticmethod
    def exists(member_id):
        session = Session()
        exists = session.query(session.query(Member).filter(Member.member_id == member_id).exists()).scalar()
        session.commit()

        return exists

    @staticmethod
    def delete(member_id):
        session = Session()
        session.delete(session.query(Member).get(member_id))
        session.commit()
    @staticmethod
    def add_member(firstname, lastname):
        session = Session()
        session.add(Member(firstname=firstname, lastname=lastname))
        session.commit()
    @staticmethod
    def get_all():
        session = Session()
        members = session.query(Member)
        session.commit()

        return members


class ClassesDAO:
    model = Class

    @staticmethod
    def get_classes():
        session = Session()
        classes = session.query(Class)
        session.commit()

        return classes

    @staticmethod
    def add(name, description, club_id):
        session = Session()
        session.add(Class(name=name, description = description, club_id=club_id))
        session.commit()


class ClubDAO:
    model = Club

    @staticmethod
    def insert_default_club():
        print("Inside insert_default_club")
        session = Session()
        session.add(Club(name='Bob', description=''))

        print("Calling session.commit()")
        session.commit()
        print("finished")

    @staticmethod
    def get_club():
        session = Session()
        return session.query(Club)[0]

    @staticmethod
    def get_club_name():
        return ClubDAO.get_club().name

    @staticmethod
    def change_club_name(new_name):
        session = Session()
        club = session.query(Club).get(ClubDAO.get_club().club_id)

        club.name = new_name
        session.commit()
