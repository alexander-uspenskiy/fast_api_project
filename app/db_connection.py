import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


# Corrected typo: `grtgev` -> `getenv`
DEV_DATABASE_URL = os.getenv("DEV_DATABASE_URL")

# The engine should be created with the DEV_DATABASE_URL
engine = create_engine(DEV_DATABASE_URL)

# Corrected bind value: pass the `engine` object instead of `True`
SessionLocal = sessionmaker(autocommit=False, autoflush=True, bind=engine)

# Corrected: `declarative_base` should be called
Base = declarative_base()

def get_db_session():
    db = SessionLocal()
    try:
        # Fixed typo: `yeld` -> `yield`
        yield db
    finally:
        db.close()

