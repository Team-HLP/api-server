from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import config

db = config.DATABASE_CONFIG
DB_URL = f"mysql+pymysql://{db['USERNAME']}:{db['PASSWORD']}@{db['HOST']}:{db['PORT']}/{db['DBNAME']}"

class engineconn:

    def __init__(self):
        self.engine = create_engine(DB_URL, pool_recycle = 500)
    
    def sessionmaker(self):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        return session
    
    def connecton(self):
        conn = self.engine.connect()
        return conn
