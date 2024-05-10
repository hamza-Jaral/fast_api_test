from sqlalchemy import create_engine, Column, Integer, String, Binary
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./webapp.db"

# Define SQLAlchemy models
Base = declarative_base()

class CVData(Base):
    __tablename__ = "cv_data"
    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String)
    pdf = Column(Binary)
    text_content = Column(String)

# Create database engine
engine = create_engine(DATABASE_URL)

# Create database session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def create_tables():
    Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
