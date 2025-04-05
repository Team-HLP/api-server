from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from motor.motor_asyncio import AsyncIOMotorClient
import config

Base = declarative_base()
mysql = config.MYSQL_CONFIG
DB_URL = f"mysql+pymysql://{mysql['USERNAME']}:{mysql['PASSWORD']}@{mysql['HOST']}:{mysql['PORT']}/{mysql['DBNAME']}?charset=utf8"

class engineconn:

    def __init__(self):
        self.engine = create_engine(DB_URL, pool_recycle=500)
    
    def sessionmaker(self):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        return session
    
    def connecton(self):
        return self.engine.connect()

def get_mysql():
    db = engineconn().sessionmaker()
    try:
        yield db
    finally:
        db.close()

engine = engineconn().engine

# Mongo DB
client = AsyncIOMotorClient(config.MONGO_URI)
mongo_db = client[config.MONGO_DB_NAME]

def get_mongodb():
    return mongo_db
