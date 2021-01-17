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
    """
    Represents the Club.
    """
    __tablename__ = 'club'
    club_id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(Text)
    members = relationship("Member", cascade="all, delete")
    classes = relationship("Class", cascade="all, delete")


class Class(Base):
    """
    Represents a class offered by the club.
    """
    __tablename__ = 'class'
    class_id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(Text)
    club_id = Column(Integer, ForeignKey('club.club_id'))
    club = relationship("Club", back_populates="classes")
    class_members = relationship("Member", secondary=class_members_table)


class Member(Base):
    """
    Represents a paying club member.
    """
    __tablename__ = 'member'
    member_id = Column(Integer, primary_key=True)
    firstname = Column(String)
    lastname = Column(String)
    club_Id = Column(Integer, ForeignKey('club.club_id'))
    club = relationship("Club", back_populates="members")


engine = create_engine('sqlite:///club.db')
Session = sessionmaker(bind=engine)


def create_db():
    """
    Creates the database if it does not exist already.
    """
    if not database_exists(engine.url):
        create_database(engine.url)
        Base.metadata.create_all(engine)
        ClubDAO.insert_default_club()
    else:
        Base.metadata.bind = engine


class MembersDAO:
    """
    Provides access to the Members database table.
    """
    model = Member

    @staticmethod
    def exists(member_id):
        """
        Returns whether or not a member with the specified id exists.
        :param member_id: The member's id
        :return: whether or not the club member exists
        """
        session = Session()
        exists = session.query(session.query(Member).filter(Member.member_id == member_id).exists()).scalar()
        session.commit()

        return exists

    @staticmethod
    def delete(member_id):
        """
        Deletes a club member
        :param member_id: The id of the club member
        """
        session = Session()
        session.delete(session.query(Member).get(member_id))
        session.commit()
    @staticmethod
    def add_member(firstname, lastname):
        """
        Adds a new member
        :param firstname: The user's first name
        :param lastname: The user's last name
        """
        session = Session()
        session.add(Member(firstname=firstname, lastname=lastname))
        session.commit()

    @staticmethod
    def get_all():
        """
        Gets all club members
        :return: the club members
        """
        session = Session()
        members = session.query(Member)
        session.commit()

        return members


class ClassesDAO:
    """
    Provides an interface to the Class database table.
    """
    model = Class

    @staticmethod
    def get_classes():
        """
        Returns all of the classes.
        :return: all of the classes
        """
        session = Session()
        classes = session.query(Class)
        session.commit()

        return classes

    @staticmethod
    def add(name, description, club_id):
        """
        Adds a new class
        :param name: The class name
        :param description: A description for the class
        :param club_id: The id of the club
        """
        session = Session()
        session.add(Class(name=name, description = description, club_id=club_id))
        session.commit()


class ClubDAO:
    """
    Provides an interface to the Club database table.
    """
    model = Club

    @staticmethod
    def insert_default_club():
        """
        Creates the default club when the database is first initialized.
        """
        print("Inside insert_default_club")
        session = Session()
        session.add(Club(name='Bob', description=''))

        print("Calling session.commit()")
        session.commit()
        print("finished")

    @staticmethod
    def get_club():
        """
        Gets the club
        :return: The club
        """
        session = Session()
        return session.query(Club)[0]

    @staticmethod
    def get_club_name():
        """
        Gets the name of the club..
        :return: the name of the club
        """
        return ClubDAO.get_club().name

    @staticmethod
    def change_club_name(new_name):
        """
        Changes the name of the club.
        :param new_name: The new name
        """
        session = Session()
        club = session.query(Club).get(ClubDAO.get_club().club_id)

        club.name = new_name
        session.commit()
