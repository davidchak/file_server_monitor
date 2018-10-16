from sqlalchemy import create_engine, Table, Column, Integer, String, Boolean, MetaData, ForeignKey
from sqlalchemy.orm import mapper, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from config import DATABASE


engine = create_engine("sqlite:///{}".format(DATABASE), echo=False)
pool_recycle = 7200
Base = declarative_base()


class Event(Base):
    __tablename__ = 'events'
    id = Column(Integer, primary_key=True)
    event = Column(String(20))
    is_directory = Column(Boolean)
    src_path = Column(String(200))
    dst_path = Column(String(200))
    time = Column(String)

    def __init__(self, event, is_directory, src_path, dst_path):
        self.event = event
        self.is_directory = is_directory
        self.src_path = src_path
        self.dst_path = dst_path
        self.time = self.get_time()

    def __repr__(self):
        return "<Event(event: {}, time: {}, is_directory: {} src: {}, dst: {})>".format(
            self.event, self.time, self.is_directory, self.src_path,
            self.dst_path
        )

    @staticmethod
    def get_time():
        time = datetime.now()
        return "{}-{}-{}".format(time.day, time.month, time.year)


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
Session.configure(bind=engine)
session = Session()