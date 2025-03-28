from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Налаштування доступу до PostgreSQL
DB_USER = "postgres"
DB_PASSWORD = "mysecretpassword"  
DB_HOST = "localhost"
DB_PORT = "5433" 
DB_NAME = "university"  

# Формування URL для SQLAlchemy
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# SQLAlchemy Engine + Session
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
