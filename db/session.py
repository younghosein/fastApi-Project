from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pyodbc
import os
from dotenv import load_dotenv

ROOT_DIR = os.path.abspath(os.curdir)
project_folder = os.path.expanduser(ROOT_DIR)
load_dotenv(os.path.join(project_folder, '.env'))

DATABASE_URL = 'mssql+pyodbc://{}:{}@{}:{}/{}?driver=SQL Server'.format(
                                                    os.getenv("DATABASE_USERNAME"),
                                                    os.getenv("DATABASE_PASSWORD"),
                                                    os.getenv("DATABASE_HOSTNAME"),
                                                    os.getenv("DATABSE_PORT"),
                                                    os.getenv("DATABASE_NAME")
                                                    )                                             
engine = create_engine(DATABASE_URL, max_overflow=-1, pool_size=0)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)