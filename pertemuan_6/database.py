from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from zope.sqlalchemy import register

# Database URL
DATABASE_URL = "sqlite:///matakuliah.db"

# Create engine
engine = create_engine(DATABASE_URL, echo=True)

# Create session factory
session_factory = sessionmaker(bind=engine)
DBSession = scoped_session(session_factory)
register(DBSession)

# Base class untuk models
Base = declarative_base()

def init_db():
    """Initialize database - create all tables"""
    Base.metadata.create_all(engine)

def get_db_session():
    """Get database session"""
    return DBSession()