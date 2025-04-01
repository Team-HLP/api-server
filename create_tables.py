from sqlalchemy import create_engine
from models import Base
import config
import datebase

engine = create_engine(datebase.DB_URL)

Base.metadata.create_all(bind=engine)
