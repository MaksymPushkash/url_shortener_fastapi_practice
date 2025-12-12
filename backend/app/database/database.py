from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from backend.app.db_config import database_config


engine = create_engine(database_config.sqlalchemy_database_url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)  # session це окремо підключення до бази,через яке ми виконуємо crud

Base = declarative_base()




