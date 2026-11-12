import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
from google.cloud.sql.connector import Connector


connector = Connector()

engine = sqlalchemy.create_engine(
    "postgresql+pg8000://",
    creator=lambda: connector.connect(
    "project-eb32ca66-0947-4573-a58:europe-west2:gardensql",
    "pg8000",
    user=os.getenv("user"),
    password=os.getenv("password"),
    db=os.getenv("dbname"),
    ip_type="public"
    ),
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
