import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Try to get the database URL from the environment variable, and fallback to a default value if not set
database_url = os.environ.get("DATABASE_URL", "sqlite:///./test.db")  # Use SQLite as the default

if not database_url:
    raise ValueError("No database URL found. Please set the DATABASE_URL environment variable.")

# Create the SQLAlchemy engine
engine = create_engine(database_url, echo=True)

# SessionLocal for handling DB sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()
