import configparser
import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

if not os.path.isdir(".database"):
    os.mkdir(".database")

config = configparser.ConfigParser()
config.read("config.ini")

engine = create_engine(config["Database"]["Route"])
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()