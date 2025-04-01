from sqlalchemy import create_engine
from models import Base
import config

db = config.DATABASE_CONFIG
DB_URL = f"mysql+pymysql://{db['USERNAME']}:{db['PASSWORD']}@{db['HOST']}:{db['PORT']}/{db['DBNAME']}"

engine = create_engine(DB_URL)

Base.metadata.create_all(bind=engine)
