from sqlalchemy import Column, Integer, String, Text, ForeignKey, Table, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from sqlalchemy_utils import database_exists, create_database

Base = declarative_base()


class_members_table = Table(
    'class_member',
    Base.metadata,
    Column('club_id', Integer, ForeignKey('club.club_id')),
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


engine = create_engine('sqlite:///club.db', echo=True)

if not database_exists(engine.url):
    create_database(engine.url)
else:
    Base.metadata.create_all(engine)
    Base.metadata.bind = engine
