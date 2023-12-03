from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

db_user = "amirashrafizham@database-fastapi-cloudnative"
db_pass = "!19Ashraf94"
db_host = "database-fastapi-cloudnative.postgres.database.azure.com"
db_port = "5432"
db_name = "bookdb"

DATABASE_URL = (
    f"postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}?sslmode=require"
)
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
