from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import config

Base = declarative_base()
db = config.DATABASE_CONFIG
DB_URL = f"mysql+pymysql://{db['USERNAME']}:{db['PASSWORD']}@{db['HOST']}:{db['PORT']}/{db['DBNAME']}?charset=utf8"

class engineconn:

    def __init__(self):
        self.engine = create_engine(DB_URL, pool_recycle=500)
    
    def sessionmaker(self):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        return session
    
    def connecton(self):
        return self.engine.connect()

def get_db():
    db = engineconn().sessionmaker()
    try:
        yield db
    finally:
        db.close()

engine = engineconn().engine
